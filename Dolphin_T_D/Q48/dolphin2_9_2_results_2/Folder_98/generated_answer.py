def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    r = list(range(a + 1, b))
    for x in t[7:-7]:
        if x in r:
            r.remove(x)
    s = sum(r)
    if s % 2:
        return bin(s)[2:]
    return hex(s)[2:].upper()