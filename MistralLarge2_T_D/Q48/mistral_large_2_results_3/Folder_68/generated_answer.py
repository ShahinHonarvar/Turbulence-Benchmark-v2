def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    present = set(t[:10])
    sum_missing = sum((x for x in range(a + 1, b) if x not in present))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]