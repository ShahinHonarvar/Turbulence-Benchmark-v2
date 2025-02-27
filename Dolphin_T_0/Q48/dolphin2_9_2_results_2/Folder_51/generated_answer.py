def return_binary_or_hexa(t):
    a, b = (t[6], t[9])
    missing = [x for x in range(a + 1, b) if x not in t[7:10]]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()