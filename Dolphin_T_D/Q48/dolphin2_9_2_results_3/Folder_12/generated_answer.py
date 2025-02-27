def return_binary_or_hexa(t):
    a = t[16]
    b = t[87]
    s = sum(range(a + 1, b)) - sum(t[17:87])
    if s % 2:
        return bin(s)[2:]
    elif s == 0:
        return ''
    else:
        return hex(s)[2:]