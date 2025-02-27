def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    r = [i for i in range(a + 1, b) if i not in t]
    if len(r) == 0:
        return ''
    s = sum(r)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]