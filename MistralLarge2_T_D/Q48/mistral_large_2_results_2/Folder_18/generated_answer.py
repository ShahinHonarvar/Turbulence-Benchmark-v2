def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    total = sum((x for x in range(a + 1, b) if x not in t[56:91]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]