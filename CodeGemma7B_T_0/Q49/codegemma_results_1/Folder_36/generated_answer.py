def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary):
        return int(binary, 2)

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_to_decimal(binary_representation)
    fib_number = fibonacci(150)
    return is_divisible(binary_to_decimal(binary_representation), fib_number)