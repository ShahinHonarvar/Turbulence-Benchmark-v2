def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    s = set(range(a + 1, b))
    s -= set(t[3:7])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]