def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal_to_binary(decimal):
        if decimal == 0:
            return '0'
        binary = ''
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal //= 2
        return binary

    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal
    binary_to_decimal(binary_str)
    for i in range(1, len(binary_str)):
        if fibonacci(i) == binary_to_decimal(binary_str):
            return True
    return False