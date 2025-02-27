def return_binary_or_hexa(t):
    a, b = (t[86], t[99])
    missing = [x for x in range(a + 1, b) if x not in t[86:99]]
    sum_missing = sum(missing)
    if not missing:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]