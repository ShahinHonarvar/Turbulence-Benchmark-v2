def if_decimal_is_divisible(binary_representation):

    def get_decimal_from_binary(binary_representation):
        decimal = 0
        for digit in binary_representation:
            decimal = decimal << 1 | int(digit)
        return decimal

    def is_divisible_by_fibonacci_16(decimal):
        fibonacci_16 = 610
        return decimal % fibonacci_16 == 0
    decimal = get_decimal_from_binary(binary_representation)
    return is_divisible_by_fibonacci_16(decimal)