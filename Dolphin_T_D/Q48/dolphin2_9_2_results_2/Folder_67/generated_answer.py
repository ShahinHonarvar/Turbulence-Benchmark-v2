def return_binary_or_hexa(t):
    a, b = (t[44], t[67])
    missing = list(set(range(a + 1, b - 1)) - set(t[44:68]))
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]