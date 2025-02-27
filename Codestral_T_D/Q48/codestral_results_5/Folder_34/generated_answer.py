def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    s = sum((x for x in range(a + 1, b) if x not in t[60 + 1:200]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]