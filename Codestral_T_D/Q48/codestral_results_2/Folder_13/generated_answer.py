def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    missing = set(range(a + 1, b)) - set(t[46:92])
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]