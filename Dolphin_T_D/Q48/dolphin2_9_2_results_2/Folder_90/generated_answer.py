def return_binary_or_hexa(t):
    a, b = (t[60], t[90])
    total = sum(set(range(a + 1, b)) - set(t[61:90]))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]