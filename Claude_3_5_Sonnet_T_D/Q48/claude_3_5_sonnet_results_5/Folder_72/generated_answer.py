def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    excluded = set(t[14:70])
    total = sum((x for x in range(a + 1, b) if x not in excluded))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]