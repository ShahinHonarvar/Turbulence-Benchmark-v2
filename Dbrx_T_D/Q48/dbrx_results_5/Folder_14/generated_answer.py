def return_binary_or_hexa(t):
    a, b = (t[2], t[5])
    present = set(t[2:6])
    missing = set(range(a + 1, b)) - present
    if not missing:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:].upper()
    else:
        return hex(sum_of_missing)[2:].upper()