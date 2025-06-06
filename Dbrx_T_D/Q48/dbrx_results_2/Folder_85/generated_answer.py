def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[1], int_tuple[8])
    missing_numbers = set(range(a + 1, b)) - set(int_tuple[1:8])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')