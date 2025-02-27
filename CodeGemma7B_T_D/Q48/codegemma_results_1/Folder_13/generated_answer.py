def return_binary_or_hexa(input_tuple):
    target_range = range(input_tuple[46] + 1, input_tuple[91] - 1)
    missing_nums = [num for num in target_range if num not in input_tuple[46:91]]
    sum_of_missing_nums = sum(missing_nums)
    if sum_of_missing_nums % 2 == 1:
        return ''.join((format(bit, 'b') for bit in bin(sum_of_missing_nums)[2:]))
    else:
        return ''.join((hex(bit)[2:].upper() for bit in hex(sum_of_missing_nums)[2:]))