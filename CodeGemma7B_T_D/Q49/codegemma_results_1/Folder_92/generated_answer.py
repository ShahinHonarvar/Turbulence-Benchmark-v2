def if_decimal_is_divisible(bin_representation):

    def recursive_fibonacci_value(binary_number, index):
        if index == 0:
            return 0
        elif index == 1:
            return 1
        else:
            return bin_to_dec(binary_number[:index]) + recursive_fibonacci_value(binary_number[index:], index - 1)

    def bin_to_dec(binary_number):
        if len(binary_number) == 1:
            return int(binary_number)
        else:
            return int(binary_number[:-1]) * 2 + int(binary_number[-1])
    return recursive_fibonacci_value(bin_representation, len(bin_representation)) % int(bin_to_dec(bin_representation[len(bin_representation) - len(str(7)):])) == 0