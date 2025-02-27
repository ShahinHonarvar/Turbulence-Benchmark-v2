def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    missing = [x for x in range(a + 1, b) if x not in t[20:44]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]