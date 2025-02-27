def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    full_range_set = set(range(a + 1, b))
    existing_range_set = set(t[21:51])
    missing_numbers_set = full_range_set - existing_range_set
    total_sum = sum(missing_numbers_set)
    if not missing_numbers_set:
        return ''
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')