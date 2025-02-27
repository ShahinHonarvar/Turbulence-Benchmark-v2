def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    if a + 1 == b - 1 and a in t and (b in t):
        return ''
    total = sum(set(range(a + 1, b)) - set(t[73:93]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()