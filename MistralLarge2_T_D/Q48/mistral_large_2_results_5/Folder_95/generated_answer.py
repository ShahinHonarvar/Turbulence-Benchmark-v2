def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    sum_missing = sum((x for x in range(a + 1, b) if x not in t[32:100]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()