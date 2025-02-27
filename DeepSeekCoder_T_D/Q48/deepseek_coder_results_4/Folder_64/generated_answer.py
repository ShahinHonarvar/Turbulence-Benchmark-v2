def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[5])
    missing_numbers = set(range(a + 1, b)) - set(tup[:6])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')