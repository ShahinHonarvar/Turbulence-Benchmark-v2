def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    s = sum((i for i in range(a + 1, b) if i not in t[18:61]))
    return bin(s)[2:] if s % 2 else hex(s)[2:].lstrip('0') if s else ''