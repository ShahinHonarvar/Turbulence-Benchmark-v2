def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    decimal = binary_to_decimal(binary_str)
    fib_47 = fibonacci(46)
    return decimal % fib_47 == 0