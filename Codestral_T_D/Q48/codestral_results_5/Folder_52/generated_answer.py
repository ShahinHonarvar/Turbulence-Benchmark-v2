def return_binary_or_hexa(t):
    a, b = (t[38], t[81])
    missing = set(range(a + 1, b)) - set(t[38 + 1:81])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''