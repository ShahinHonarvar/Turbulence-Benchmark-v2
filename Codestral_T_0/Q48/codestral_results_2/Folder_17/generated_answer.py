def return_binary_or_hexa(t):
    a = t[73]
    b = t[84]
    missing = set(range(a + 1, b)) - set(t[73 + 1:84])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''