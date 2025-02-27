def return_binary_or_hexa(t):
    a, b = (t[3], t[9])
    sum_missing = sum((x for x in range(a + 1, b) if x not in t[3:10]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]