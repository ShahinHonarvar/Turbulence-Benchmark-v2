def return_binary_or_hexa(t):
    a, b = (t[0], t[9])
    s = sum((i for i in range(a + 1, b) if i not in t))
    return bin(s)[2:] if s % 2 else hex(s)[2:]