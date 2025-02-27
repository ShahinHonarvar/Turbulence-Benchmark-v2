def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    existing = set(tup[38:53])
    sum_missing = sum((x for x in range(a + 1, b) if x not in existing))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]