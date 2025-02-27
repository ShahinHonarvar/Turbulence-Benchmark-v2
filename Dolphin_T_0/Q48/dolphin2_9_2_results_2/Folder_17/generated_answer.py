def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    s = sum(range(a + 1, b))
    for i in range(74, 85):
        if t[i] in range(a + 1, b):
            s -= t[i]
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]