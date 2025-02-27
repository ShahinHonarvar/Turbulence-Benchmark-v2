def if_decimal_is_divisible(binary):
    fibs = [1, 1]
    fib_num = 2
    while fib_num <= int(binary, 2):
        fibs.append(fib_num)
        fib_num += fibs[-2] + fibs[-1]
    for num in fibs:
        if num % 105 == 0 and int(binary, 2) % num == 0:
            return True
    return False