def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    missing = [i for i in range(a + 1, b) if i not in t]
    if len(missing) == 0:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]