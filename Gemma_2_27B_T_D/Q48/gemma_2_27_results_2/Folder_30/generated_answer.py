def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    s = sum([x for x in range(a + 1, b) if x not in t[22:25]])
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]