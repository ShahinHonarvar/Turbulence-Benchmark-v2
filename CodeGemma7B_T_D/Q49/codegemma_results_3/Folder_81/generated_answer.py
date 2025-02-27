def if_decimal_is_divisible(n):
    fib = 1
    fib_list = [fib]
    while fib_list[-1] <= int(n, 2):
        fib_list.append(fib)
        fib = fib_list[-1] + fib_list[-2]
    result = int(n, 2)
    for i, j in enumerate(fib_list):
        if j == result % fib_list[i]:
            if i >= 24 and fib_list[i + 1] + fib_list[i - 1] == result % (fib_list[i + 1] + fib_list[i - 1]):
                return True
    return False