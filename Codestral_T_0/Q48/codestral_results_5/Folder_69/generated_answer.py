def return_binary_or_hexa(t):
    a, b = (t[39], t[43])
    s = sum((i for i in range(a + 1, b) if i not in t[39:43]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]