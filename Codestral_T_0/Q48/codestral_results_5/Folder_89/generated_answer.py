def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    s = sum((i for i in range(a + 1, b) if i not in t[55:84]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]