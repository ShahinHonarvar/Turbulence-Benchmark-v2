def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    sum_missing = sum(set(range(a + 1, b)) - set(t[35:65]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]