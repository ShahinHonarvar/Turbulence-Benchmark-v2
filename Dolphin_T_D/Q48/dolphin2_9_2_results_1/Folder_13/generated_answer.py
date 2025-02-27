def return_binary_or_hexa(t):
    a, b = (t[46], t[91])
    missing = [x for x in range(a + 1, b) if x not in t]
    s = sum(missing)
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]