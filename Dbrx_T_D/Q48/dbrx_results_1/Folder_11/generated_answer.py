def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    missing = set(range(a + 1, b)) - set(t[48:76 + 1])
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()