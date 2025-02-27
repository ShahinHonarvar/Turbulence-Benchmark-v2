def if_decimal_is_divisible(binary_str):
    fib_a, fib_b = (0, 1)
    for _ in range(133):
        fib_a, fib_b = (fib_b, fib_a + fib_b)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_b == 0