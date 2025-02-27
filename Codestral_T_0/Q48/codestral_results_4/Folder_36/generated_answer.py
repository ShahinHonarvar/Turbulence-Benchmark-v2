def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    s = sum((i for i in range(a + 1, b) if i not in t[110:349]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]