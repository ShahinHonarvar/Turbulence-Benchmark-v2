def return_binary_or_hexa(t):
    a = t[13]
    b = t[91]
    missing = set(range(a + 1, b)) - set(t[13 + 1:91])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''