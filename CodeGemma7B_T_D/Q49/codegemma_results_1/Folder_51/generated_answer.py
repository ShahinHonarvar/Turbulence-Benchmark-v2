def if_decimal_is_divisible(binary):
    if len(binary) == 1 and int(binary, 2) == 0:
        return True
    if len(binary) == 1 and int(binary, 2) > 0:
        return False
    fib_list = [0, 1]
    for i in range(2, 25):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    for num in fib_list:
        if num % binary == 0:
            return True
    return False