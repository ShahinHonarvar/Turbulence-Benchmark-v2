def return_binary_or_hexa(t):
    a, b = (t[86], t[99])
    existing = set(t[86:100])
    total = sum((x for x in range(a + 1, b) if x not in existing))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]