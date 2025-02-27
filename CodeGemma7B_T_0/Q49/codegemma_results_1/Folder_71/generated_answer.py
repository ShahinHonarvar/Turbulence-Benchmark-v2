def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary_string):
        decimal = 0
        for i, bit in enumerate(binary_string):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(decimal, divisor):
        return decimal % divisor == 0
    binary_to_decimal_value = binary_to_decimal(binary_string)
    fibonacci_value = fibonacci(147)
    return is_divisible(binary_to_decimal_value, fibonacci_value)