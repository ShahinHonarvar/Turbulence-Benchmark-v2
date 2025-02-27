def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[39]
    b = sorted_tuple[43]
    missing_numbers = [i for i in range(a + 1, b) if i not in sorted_tuple[39:44]]
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, '08b')
    else:
        return format(sum_of_missing, '02x').upper()