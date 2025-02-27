def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    present = set(t[2:6])
    missing = [i for i in range(a + 1, b) if i not in present]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()