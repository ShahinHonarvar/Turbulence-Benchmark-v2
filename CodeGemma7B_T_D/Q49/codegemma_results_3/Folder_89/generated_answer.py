import math

def if_decimal_is_divisible(binary_representation):

    def get_fibonacci_number(index):
        if index == 0:
            return 0
        elif index == 1:
            return 1
        else:
            return get_fibonacci_number(index - 1) + get_fibonacci_number(index - 2)

    def get_decimal_value(binary_representation):
        decimal_value = 0
        for i, digit in enumerate(binary_representation):
            decimal_value += int(digit) * math.pow(2, i)
        return decimal_value
    fibonacci_number = get_fibonacci_number(126)
    decimal_value = get_decimal_value(binary_representation)
    return decimal_value % fibonacci_number == 0