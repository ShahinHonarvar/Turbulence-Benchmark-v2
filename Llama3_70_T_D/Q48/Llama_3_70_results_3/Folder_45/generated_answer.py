def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    s = sum((i for i in range(a + 1, b) if i not in t[30:201]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]