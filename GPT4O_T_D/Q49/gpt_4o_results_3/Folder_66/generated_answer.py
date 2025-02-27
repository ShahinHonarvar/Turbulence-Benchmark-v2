def if_decimal_is_divisible(binary_str):
    binary_str = binary_str.strip()
    decimal_number = int(binary_str, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    fib_120th = fibonacci(120)
    return decimal_number % fib_120th == 0