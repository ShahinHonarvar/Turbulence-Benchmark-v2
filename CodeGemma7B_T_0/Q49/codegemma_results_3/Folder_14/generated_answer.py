def if_decimal_is_divisible(binary_representation):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_to_binary(decimal):
        if decimal == 0:
            return '0'
        binary = ''
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        return binary

    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal

    def get_nth_fibonacci(n):
        if n < 1:
            raise ValueError('Invalid input: n must be greater than or equal to 1')
        return fibonacci(n - 1)

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_representation = binary_representation[::-1]
    decimal = binary_to_decimal(binary_representation)
    nth_fibonacci = get_nth_fibonacci(27)
    return is_divisible(decimal, nth_fibonacci)