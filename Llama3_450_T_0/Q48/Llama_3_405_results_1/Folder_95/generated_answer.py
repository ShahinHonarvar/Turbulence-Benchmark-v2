def return_binary_or_hexa(t):
    a = t[32]
    b = t[99]
    s = set(range(a + 1, b))
    s -= set(t[33:99])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]