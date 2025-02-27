def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    s = sum(set(range(a + 1, b + 1)) - set(t[50:75]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]