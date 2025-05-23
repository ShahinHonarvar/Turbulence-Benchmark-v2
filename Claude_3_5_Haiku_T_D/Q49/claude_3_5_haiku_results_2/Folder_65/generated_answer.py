def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_127 = fibonacci(127)
    decimal_number = binary_to_decimal(binary_string)
    return decimal_number % fib_127 == 0