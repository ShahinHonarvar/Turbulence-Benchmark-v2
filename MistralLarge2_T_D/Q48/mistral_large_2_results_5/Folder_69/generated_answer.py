def return_binary_or_hexa(t):
    a, b = (t[39], t[43])
    sum_missing = sum(set(range(a + 1, b)) - set(t[39:44]))
    if not sum_missing:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]