def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    missing = [i for i in range(a + 1, b) if i not in t[56:89]]
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()