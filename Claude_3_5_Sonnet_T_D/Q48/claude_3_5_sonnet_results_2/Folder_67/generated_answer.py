def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    excluded = set(t[44:68])
    total = sum((x for x in range(a + 1, b) if x not in excluded))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]