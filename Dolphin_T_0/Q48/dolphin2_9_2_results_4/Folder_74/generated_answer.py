def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    s = sum(set(range(a + 1, b)) - set(t[70:97]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]