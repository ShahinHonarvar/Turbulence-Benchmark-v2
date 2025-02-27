def return_binary_or_hexa(input_tuple):
    a = input_tuple[56]
    b = input_tuple[90]
    present_numbers = set(input_tuple[56:91])
    missing_numbers = set(range(a + 1, b)) - present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()