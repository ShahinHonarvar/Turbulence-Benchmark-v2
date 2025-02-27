def return_binary_or_hexa(t):
    a = t[40]
    b = t[200]
    s = sum((i for i in range(a + 1, b) if i not in t[40:201]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()