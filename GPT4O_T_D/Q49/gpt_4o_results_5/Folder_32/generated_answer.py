def if_decimal_is_divisible(binary_str):
    fib_a, fib_b = (0, 1)
    for _ in range(177):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_b == 0