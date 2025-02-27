def return_binary_or_hexa(t):
    a, b = (t[3], t[9])
    missing = set(range(a + 1, b)).difference(t[3:10])
    if not missing:
        return ''
    total = sum(missing)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()