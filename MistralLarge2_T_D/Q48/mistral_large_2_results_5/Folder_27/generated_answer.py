def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    sum_missing = sum(set(range(a + 1, b)) - set(tup[86:89 + 1]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]