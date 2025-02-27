def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    missing = set(range(a + 1, b)) - set(t[:10])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''