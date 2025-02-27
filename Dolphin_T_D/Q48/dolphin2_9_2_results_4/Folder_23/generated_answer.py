def return_binary_or_hexa(t):
    a = t[20]
    b = t[36]
    missing = set(range(a + 1, b)) - set(t[21:36])
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return bin(s)[2:]
    return hex(s)[2:].lower()