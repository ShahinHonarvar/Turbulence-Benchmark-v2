def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    s = sum((i for i in range(a + 1, b) if i not in t[49:74]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]