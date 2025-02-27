def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    missing = [i for i in range(a + 1, b) if i not in t[39:52]]
    sum_missing = sum(missing)
    if len(missing) == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]