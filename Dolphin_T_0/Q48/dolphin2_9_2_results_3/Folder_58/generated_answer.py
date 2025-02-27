def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    s = sum(set(range(a + 1, b)) - set(t[276:871]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]