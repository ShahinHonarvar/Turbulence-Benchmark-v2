def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = sum(set(range(a + 1, b)) - set(t[34:70]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]