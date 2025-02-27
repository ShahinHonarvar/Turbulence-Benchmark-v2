def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary_str):
        decimal = 0
        for i, bit in enumerate(binary_str):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_to_decimal_int = binary_to_decimal(binary_str)
    fibonacci_160th = fibonacci(160)
    return is_divisible(binary_to_decimal_int, fibonacci_160th)