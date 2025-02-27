def return_binary_or_hexa(t):
    a, b = (t[68], t[99])
    missing = [x for x in range(a + 1, b) if x not in t]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]