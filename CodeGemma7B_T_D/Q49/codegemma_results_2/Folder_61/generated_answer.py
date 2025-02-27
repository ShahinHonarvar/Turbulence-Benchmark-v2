def if_decimal_is_divisible(binary):

    def is_divisible_by_fibonacci(decimal):
        a, b = (0, 1)
        while True:
            if decimal == 0:
                return False
            elif decimal == a:
                return True
            elif decimal < a:
                a, b = (b, a + b)
            else:
                a, b = (a + b, b)

    def get_decimal_from_binary(binary):
        decimal = 0
        for i, digit in enumerate(binary):
            decimal += int(digit) * 2 ** (len(binary) - i - 1)
        return decimal
    binary_reversed = binary[::-1]
    decimal = get_decimal_from_binary(binary_reversed)
    return is_divisible_by_fibonacci(decimal)