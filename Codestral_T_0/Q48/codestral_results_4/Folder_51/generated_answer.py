def return_binary_or_hexa(t):
    a, b = (t[6], t[9])
    missing = set(range(a + 1, b)) - set(t[6:9])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''