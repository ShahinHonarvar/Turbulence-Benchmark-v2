def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    s = sum((i for i in range(a + 1, b) if i not in t[22:25]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]