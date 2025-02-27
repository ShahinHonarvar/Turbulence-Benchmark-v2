def return_binary_or_hexa(t):
    a = t[50]
    b = t[200]
    s = set(range(a + 1, b))
    s -= set(t[51:200])
    total = sum(s)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]