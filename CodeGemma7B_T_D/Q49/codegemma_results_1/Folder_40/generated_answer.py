def if_decimal_is_divisible(binary_string):

    def get_fibonacci_for_index(index):
        if index == 0:
            return 0
        elif index == 1:
            return 1
        else:
            return get_fibonacci_for_index(index - 1) + get_fibonacci_for_index(index - 2)

    def get_nth_bit(binary_string, n):
        return int(binary_string[-n])
    decimal_integer_representation = 0
    for index, bit in enumerate(binary_string):
        if int(bit) == 1:
            decimal_integer_representation += get_nth_bit(binary_string, index + 1) * 2 ** (len(binary_string) - index - 1)
    for index in range(4):
        if get_fibonacci_for_index(index) == decimal_integer_representation:
            return True
    return False