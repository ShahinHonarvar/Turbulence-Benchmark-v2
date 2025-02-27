def return_binary_or_hexa(t):
    a, b = (t[13], t[91])
    s = sum((i for i in range(a + 1, b) if i not in t[13:92]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]