def if_decimal_is_divisible(binary_representation):

    def binary_to_decimal(binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    binary_decimal = binary_to_decimal(binary_representation)
    return binary_decimal % fibonacci(186) == 0