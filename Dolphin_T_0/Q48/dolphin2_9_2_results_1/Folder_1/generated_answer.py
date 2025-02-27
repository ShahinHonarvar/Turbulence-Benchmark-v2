def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    missing = []
    if a == b:
        return ''
    for i in range(a + 1, b):
        if i not in t[17:89]:
            missing.append(i)
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]