def return_binary_or_hexa(input_tuple):
    a = input_tuple[35]
    b = input_tuple[64]
    sum_of_missing_ints = sum(set(range(a + 1, b)) - set(input_tuple[35:65]))
    if sum_of_missing_ints % 2 != 0:
        binary_representation = format(sum_of_missing_ints, 'b')
        return binary_representation
    else:
        hexadecimal_representation = format(sum_of_missing_ints, 'x')
        return hexadecimal_representation