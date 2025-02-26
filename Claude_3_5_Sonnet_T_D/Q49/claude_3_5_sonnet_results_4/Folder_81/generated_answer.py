def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 1:
            return n
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b
    decimal = int(binary_str, 2)
    fib_97 = fibonacci(97)
    return decimal % fib_97 == 0