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
            if decimal % 2 == 0:
                binary = '0' + binary
            else:
                binary = '1' + binary
            decimal //= 2
        return binary

    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            if bit == '1':
                decimal += 2 ** i
        return decimal

    def get_nth_fibonacci(n):
        if n <= 0:
            return None
        return fibonacci(n - 1)
    binary_length = len(binary_representation)
    if binary_length < 146:
        return False
    binary_representation = binary_representation[:146]
    decimal = binary_to_decimal(binary_representation)
    nth_fibonacci = get_nth_fibonacci(146)
    if nth_fibonacci is None:
        return False
    return decimal % nth_fibonacci == 0