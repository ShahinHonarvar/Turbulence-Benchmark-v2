def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    s = sum((i for i in range(a + 1, b) if i not in t[33:79]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]