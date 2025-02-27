def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        a, b = (0, 1)
        for _ in range(n):
            a, b = (b, a + b)
        return a

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)
    decimal_number = binary_to_decimal(binary_string)
    fib_number = fibonacci(105)
    return decimal_number % fib_number == 0