def return_binary_or_hexa(t):
    a, b = (t[56], t[88])
    missing = [i for i in range(a + 1, b) if i not in t[56:89]]
    sum_missing = sum(missing)
    if not missing:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]