def return_binary_or_hexa(t):
    a = t[0]
    b = t[3]
    s = sum([i for i in range(a + 1, b) if i not in t[:4]])
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()