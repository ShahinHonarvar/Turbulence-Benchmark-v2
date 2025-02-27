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
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal //= 2
        return binary

    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal
    binary_representation = binary_representation.replace(' ', '')
    binary_representation = binary_representation.replace('0b', '')
    binary_representation = binary_representation.replace('0B', '')
    decimal = binary_to_decimal(binary_representation)
    index = 0
    while True:
        if fibonacci(index) > decimal:
            break
        index += 1
    if fibonacci(index) % decimal == 0:
        return True
    return False