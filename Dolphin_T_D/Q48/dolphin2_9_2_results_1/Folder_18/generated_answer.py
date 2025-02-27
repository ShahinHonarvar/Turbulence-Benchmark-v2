def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    missing = []
    for i in range(a + 1, b):
        if not t[56:90 + 1].__contains__(i):
            missing.append(i)
    if len(missing) == 0:
        return ''
    total = sum(missing)
    if total % 2 == 0:
        return hex(total).replace('0x', '').upper()
    else:
        return bin(total).replace('0b', '')