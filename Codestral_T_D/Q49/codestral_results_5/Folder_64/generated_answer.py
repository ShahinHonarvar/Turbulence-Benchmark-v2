def if_decimal_is_divisible(binary_str):

    def get_fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a
    decimal = int(binary_str, 2)
    fibonacci_10th = get_fibonacci(10)
    return decimal % fibonacci_10th == 0