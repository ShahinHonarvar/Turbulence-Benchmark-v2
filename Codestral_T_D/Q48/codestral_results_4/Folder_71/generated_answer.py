def return_binary_or_hexa(t):
    a, b = (t[20], t[35])
    s = sum((i for i in range(a + 1, b) if i not in t[20:36]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''