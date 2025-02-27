def return_binary_or_hexa(t):
    a = t[0]
    b = t[3]
    missing = []
    for i in range(a + 1, b):
        if i not in t:
            missing.append(i)
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]