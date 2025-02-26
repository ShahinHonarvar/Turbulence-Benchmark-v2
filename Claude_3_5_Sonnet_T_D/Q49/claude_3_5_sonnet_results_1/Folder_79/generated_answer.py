def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fib_a, fib_b = (0, 1)
    for _ in range(12):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    return decimal % fib_b == 0