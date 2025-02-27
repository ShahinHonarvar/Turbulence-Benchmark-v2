def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    s = sum(range(a + 1, b)) - sum(t[44 + 1:91])
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]