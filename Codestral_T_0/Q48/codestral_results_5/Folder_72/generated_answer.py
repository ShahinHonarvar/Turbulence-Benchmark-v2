def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    s = sum((i for i in range(a + 1, b) if i not in t[13:70]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]