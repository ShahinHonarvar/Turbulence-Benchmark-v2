def return_binary_or_hexa(t):
    a, b = (t[0], t[10])
    sum_missing = sum((x for x in range(a + 1, b) if x not in t[:11]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()