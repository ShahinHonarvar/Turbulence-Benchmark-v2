def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    s = sum((i for i in range(a + 1, b) if i not in t[275:872]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]