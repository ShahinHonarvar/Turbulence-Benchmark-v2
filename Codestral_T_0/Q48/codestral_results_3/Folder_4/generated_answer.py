def return_binary_or_hexa(t):
    a, b = (t[49], t[74])
    s = sum((i for i in range(a + 1, b) if i not in t[49:74]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]