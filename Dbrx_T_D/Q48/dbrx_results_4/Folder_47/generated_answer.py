def return_binary_or_hexa(t):
    a, b = (t[29], t[53])
    if a + 1 >= b - 1:
        return ''
    missing = set(range(a + 1, b)) - set(t[29:54])
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()