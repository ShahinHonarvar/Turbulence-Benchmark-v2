def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    full_range = set(range(a + 1, b))
    existing_range = set(t[1:3])
    missing_numbers = full_range - existing_range
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return '{:x}'.format(sum_missing)
    else:
        return '{:b}'.format(sum_missing)