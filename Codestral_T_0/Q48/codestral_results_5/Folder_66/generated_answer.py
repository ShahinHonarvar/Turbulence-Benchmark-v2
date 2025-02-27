def return_binary_or_hexa(t):
    a, b = (t[11], t[76])
    s = sum((i for i in range(a + 1, b) if i not in t[11:77]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]