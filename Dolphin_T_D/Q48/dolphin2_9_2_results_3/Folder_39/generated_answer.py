def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    m = set(t[45:91])
    s = sum((i for i in range(a + 1, b) if i not in m))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()