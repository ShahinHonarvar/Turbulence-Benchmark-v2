def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    s = sum(range(a + 1, b)) - sum(t[73:93])
    if s == 0:
        return ''
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]