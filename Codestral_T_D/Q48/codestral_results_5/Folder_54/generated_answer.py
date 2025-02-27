def return_binary_or_hexa(t):
    a, b = (t[35], t[64])
    s = sum((i for i in range(a + 1, b) if i not in t[35:64]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]