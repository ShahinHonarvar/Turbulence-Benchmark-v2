def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_a, fib_b = (0, 1)
    for _ in range(158):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    return decimal_number % fib_b == 0