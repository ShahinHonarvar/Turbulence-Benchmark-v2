def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = (0, 1)
            for _ in range(2, n + 1):
                a, b = (b, a + b)
            return b

    def binary_to_decimal(binary_string):
        decimal = 0
        for i, bit in enumerate(binary_string[::-1]):
            decimal += int(bit) * 2 ** i
        return decimal
    fibonacci_number = fibonacci(45)
    decimal = binary_to_decimal(binary_string)
    return decimal % fibonacci_number == 0