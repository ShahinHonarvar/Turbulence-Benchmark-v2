def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    sum_missing = sum((x for x in range(a + 1, b) if x not in t[44:68]))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 != 0 else hex(sum_missing)[2:]