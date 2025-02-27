def return_binary_or_hexa(tup):
    a = tup[30]
    b = tup[200]
    missing = set(range(a + 1, b)) - set(tup[30:201])
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]