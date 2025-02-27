def return_binary_or_hexa(indices):
    a = indices[57]
    b = indices[85]
    present_numbers = set(indices[57:86])
    missing_numbers = set(range(a + 1, b))
    missing_numbers.difference_update(present_numbers)
    if not missing_numbers:
        return ''
    else:
        sum_missing = sum(missing_numbers)
        if sum_missing % 2:
            return format(sum_missing, '08b')
        else:
            return format(sum_missing, '02x').upper()