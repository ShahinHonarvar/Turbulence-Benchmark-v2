def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[1], input_tuple[8])
    present_set = set(input_tuple[1:8])
    missing_numbers = set(range(a + 1, b)) - present_set
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()