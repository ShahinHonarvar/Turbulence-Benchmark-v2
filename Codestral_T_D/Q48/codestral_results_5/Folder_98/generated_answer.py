def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing = set(range(a + 1, b)) - set(t[6:7])
    total = sum(missing)
    if not missing:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]