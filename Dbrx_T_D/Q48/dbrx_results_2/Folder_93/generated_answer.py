def return_binary_or_hexa(input_tuple):
    a = input_tuple[57]
    b = input_tuple[85]
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[57:85 + 1])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()