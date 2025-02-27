def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[0], int_tuple[8])
    present_numbers = set(int_tuple[1:8] + int_tuple[9:])
    missing_numbers = set(range(a + 1, b)) - present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()