def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    s = sum(range(a + 1, b))
    for i in range(451, 906):
        if t[i] in range(a + 1, b):
            s -= t[i]
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()
    return ''