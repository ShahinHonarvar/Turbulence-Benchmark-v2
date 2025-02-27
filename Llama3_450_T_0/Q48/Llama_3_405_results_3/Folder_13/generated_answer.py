def return_binary_or_hexa(t):
    a = t[46]
    b = t[91]
    s = set(range(a + 1, b))
    s -= set(t[47:91])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]