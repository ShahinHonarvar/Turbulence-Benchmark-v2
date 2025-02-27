def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    vals = t[58:85]
    exist = all((x in vals for x in range(a + 1, b)))
    if exist:
        return ''
    total = sum((x for x in range(a + 1, b + 1) if x not in vals))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]