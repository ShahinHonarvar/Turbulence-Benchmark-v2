def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    s = sum(set(range(a + 1, b)) - set(t[44:79]))
    if s == 0:
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]