def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[6])
    missing = set(range(a + 1, b)) - set(tup[:7])
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]