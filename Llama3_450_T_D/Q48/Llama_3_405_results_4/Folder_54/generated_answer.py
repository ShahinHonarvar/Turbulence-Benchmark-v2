def return_binary_or_hexa(t):
    a = t[35]
    b = t[64]
    s = set(range(a + 1, b))
    missing = s - set(t[36:64])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]