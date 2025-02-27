def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    s = set(range(a + 1, b))
    s -= set(t[82:86])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]