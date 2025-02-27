def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    s = sum((i for i in range(a + 1, b) if i not in t[25:81]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]