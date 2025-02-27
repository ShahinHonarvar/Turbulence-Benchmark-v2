def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fib_a, fib_b = (0, 1)
    for _ in range(76):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    return decimal_integer % fib_b == 0