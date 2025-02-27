def return_binary_or_hexa(t):
    a, b = (t[20], t[51])
    s = sum((i for i in range(a + 1, b) if i not in t[20:52]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper() if s else ''