def return_binary_or_hexa(t):
    a = t[3]
    b = t[9]
    s = set(range(a + 1, b))
    s -= set(t[4:9])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]