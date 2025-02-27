def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    s = set(range(a + 1, b))
    s -= set(t[276:871])
    total = sum(s)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]