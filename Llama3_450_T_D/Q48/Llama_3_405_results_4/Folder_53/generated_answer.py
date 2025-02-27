def return_binary_or_hexa(t):
    a = t[200]
    b = t[202]
    s = set(range(a + 1, b))
    s -= set(t[201:202])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]