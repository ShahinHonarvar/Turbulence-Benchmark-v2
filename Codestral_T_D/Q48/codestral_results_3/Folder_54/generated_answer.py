def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    missing = set(range(a + 1, b)) - set(t[35 + 1:64])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]