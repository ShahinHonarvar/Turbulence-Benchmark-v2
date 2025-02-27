def if_decimal_is_divisible(binary_str):
    i = 1
    fib_16 = 0
    while i <= 16:
        if i <= 2:
            fib_16 = 1
        else:
            fib_16 = fib_16 + fib_16 - 1
        i += 1
    return int(binary_str, 2) % fib_16 == 0