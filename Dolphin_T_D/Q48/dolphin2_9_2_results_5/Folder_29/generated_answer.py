def return_binary_or_hexa(t):
    a = t[70]
    b = t[98]
    s = sum(set(range(a + 1, b)) - set(t[71:98]))
    if s == 0:
        return ''
    if s & 1 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]