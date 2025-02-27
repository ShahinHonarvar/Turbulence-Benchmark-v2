def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    s = sum((i for i in range(a + 1, b) if i not in set(t[6:8])))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper()