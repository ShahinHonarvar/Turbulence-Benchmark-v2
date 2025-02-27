def return_binary_or_hexa(integer_tuple):
    a, b = (integer_tuple[0], integer_tuple[10])
    missing_numbers = set(range(a + 1, b)) - set(integer_tuple[1:10])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()