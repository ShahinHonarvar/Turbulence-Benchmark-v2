def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary):
        return int(binary, 2)
    fib_68 = fibonacci(68)
    decimal = binary_to_decimal(binary_string)
    return decimal % fib_68 == 0