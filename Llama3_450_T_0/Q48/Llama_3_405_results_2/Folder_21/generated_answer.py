def return_binary_or_hexa(t):
    a = t[15]
    b = t[57]
    s = set(range(a + 1, b))
    s -= set(t[16:57])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]