def return_binary_or_hexa(t):
    a, b = (t[25], t[80])
    missing = set(range(a + 1, b)) - set(t[25 + 1:80])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''