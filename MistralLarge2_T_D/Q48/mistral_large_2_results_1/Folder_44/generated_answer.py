def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    subset = set(t[36:53])
    s = sum((x for x in range(a + 1, b) if x not in subset))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]