def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    missing = [i for i in range(a + 1, b) if i not in t[40:43]]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 != 0:
        return bin(s)[2:]
    return hex(s)[2:]