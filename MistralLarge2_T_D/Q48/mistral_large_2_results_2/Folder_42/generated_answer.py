def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    sum_missing = sum((i for i in range(a + 1, b) if i not in t[18:61]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()