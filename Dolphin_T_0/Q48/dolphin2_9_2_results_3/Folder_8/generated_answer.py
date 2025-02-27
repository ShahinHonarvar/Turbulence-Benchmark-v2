def return_binary_or_hexa(t):
    a = t[45]
    b = t[48]
    s = sum((i for i in range(a + 1, b) if i not in t[45:49]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]