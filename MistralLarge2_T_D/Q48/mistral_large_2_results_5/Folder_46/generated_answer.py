def return_binary_or_hexa(t):
    a, b = (t[10], t[79])
    existing = set(t[10:80])
    total = sum((x for x in range(a + 1, b) if x not in existing))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]