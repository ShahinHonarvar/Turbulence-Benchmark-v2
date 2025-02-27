def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = sum((x for x in range(a + 1, b) if x not in t[35:69]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()