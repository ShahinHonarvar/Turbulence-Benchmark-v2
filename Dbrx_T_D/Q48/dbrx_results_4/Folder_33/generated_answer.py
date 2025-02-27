def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[13]
    b = numbers_tuple[35]
    missing_numbers = set(range(a + 1, b)) - set(numbers_tuple[13:35])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()