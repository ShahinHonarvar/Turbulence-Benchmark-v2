def return_binary_or_hexa(t):
    a = t[48]
    b = t[76]
    missing = set(range(a + 1, b)) - set(t[48:76])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''