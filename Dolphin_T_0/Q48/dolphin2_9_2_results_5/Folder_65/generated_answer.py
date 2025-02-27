def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    if all((i in t for i in range(a + 1, b))):
        return ''
    vals = [x for x in range(a + 1, b) if x not in t]
    total = sum(vals)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]