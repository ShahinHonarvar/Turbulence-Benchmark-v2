def return_binary_or_hexa(tup):
    a, b = (tup[10], tup[97])
    missing = set(range(a + 1, b)) - set(tup[11:97])
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2:
        return format(sum_missing, '08b')
    else:
        return format(sum_missing, '02x').upper()