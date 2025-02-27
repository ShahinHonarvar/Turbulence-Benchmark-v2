def if_decimal_is_divisible(binary_string):

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n - 1):
            a, b = (b, a + b)
        return a
    decimal = binary_to_decimal(binary_string)
    fib_number = fibonacci(9)
    return decimal % fib_number == 0