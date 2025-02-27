def if_decimal_is_divisible(binary_string):

    def get_fibonacci(pos):
        if pos <= 1:
            return pos
        else:
            return get_fibonacci(pos - 1) + get_fibonacci(pos - 2)

    def get_decimal_from_binary(binary_string):
        decimal_value = 0
        for i, bit in enumerate(binary_string):
            decimal_value += int(bit) * 2 ** (len(binary_string) - i - 1)
        return decimal_value
    binary_index = get_fibonacci(105) - 1
    if len(binary_string) < binary_index:
        return False
    binary_value = binary_string[len(binary_string) - binary_index:]
    decimal_value = get_decimal_from_binary(binary_value)
    return decimal_value % 105 == 0