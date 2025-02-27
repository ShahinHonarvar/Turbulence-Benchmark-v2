def if_decimal_is_divisible(binary_str):
    fib_a, fib_b = (0, 1)
    for _ in range(106):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_b == 0