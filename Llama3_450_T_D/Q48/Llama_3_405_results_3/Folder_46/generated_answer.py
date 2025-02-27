def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    s = set(range(a + 1, b))
    s -= set(t[11:80])
    total = sum(s)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''