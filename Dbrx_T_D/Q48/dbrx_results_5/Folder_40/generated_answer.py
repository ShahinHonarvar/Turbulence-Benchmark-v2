def return_binary_or_hexa(t):
    a, _, _, b = t
    missing = set(range(a + 1, b)) - set(t[1:-1])
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()