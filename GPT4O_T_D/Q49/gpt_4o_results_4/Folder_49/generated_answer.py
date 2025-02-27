def if_decimal_is_divisible(binary_string):
    binary_to_decimal = int(binary_string, 2)
    fib_94, fib_95 = (0, 1)
    for _ in range(94):
        fib_94, fib_95 = (fib_95, fib_94 + fib_95)
    return binary_to_decimal % fib_95 == 0