def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_1, fib_2 = (0, 1)
    for _ in range(106):
        fib_1, fib_2 = (fib_2, fib_1 + fib_2)
    return decimal % fib_2 == 0