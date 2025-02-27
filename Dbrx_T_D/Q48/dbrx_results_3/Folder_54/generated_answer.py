def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    present = set(t[35:65])
    missing = set(range(a + 1, b)) - present
    sum_missing = sum(missing)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()