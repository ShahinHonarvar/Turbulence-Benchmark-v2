def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    missing = set(range(a + 1, b)) - set(t[427:669])
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]