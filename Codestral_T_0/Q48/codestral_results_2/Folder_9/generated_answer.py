def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    s = sum((i for i in range(a + 1, b) if i not in t[70:201]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]