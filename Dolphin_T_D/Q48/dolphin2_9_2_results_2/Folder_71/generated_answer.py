def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    if all((x in t[20:36] for x in range(a + 1, b))):
        return ''
    total = sum((x for x in range(a + 1, b) if x not in t[20:36]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]