def return_binary_or_hexa(int_tuple):
    a = int_tuple[450]
    b = int_tuple[905]
    missing_numbers = set(range(a + 1, b)) - set(int_tuple[450:906])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()