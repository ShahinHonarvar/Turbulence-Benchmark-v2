def if_decimal_is_divisible(binary):
    result = int(binary, 2)
    fib = 0
    fib_list = [0, 1]
    while result >= fib:
        fib = fib_list[-2] + fib_list[-1]
        fib_list.append(fib)
    if result == fib_list[-2]:
        return True
    else:
        return False