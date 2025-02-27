def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    missing = [x for x in range(a + 1, b) if x not in t]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]