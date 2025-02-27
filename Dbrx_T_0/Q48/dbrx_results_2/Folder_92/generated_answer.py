def return_binary_or_hexa(input_tuple):
    a, _, b = input_tuple
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[1])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()