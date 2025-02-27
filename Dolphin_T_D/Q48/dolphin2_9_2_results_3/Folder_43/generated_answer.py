def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    s = sum(set(range(a + 1, b)) - set(t[11:28]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s != 0:
        return hex(s)[2:]
    else:
        return ''