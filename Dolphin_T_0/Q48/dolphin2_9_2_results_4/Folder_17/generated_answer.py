def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    s = sum(set(range(a + 1, b)) - set(t[74:84]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]