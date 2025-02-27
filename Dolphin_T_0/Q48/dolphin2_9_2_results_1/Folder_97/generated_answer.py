def return_binary_or_hexa(t):
    a = t[34]
    b = t[69]
    s = sum(range(a + 1, b))
    if all((i in t[35:69] for i in range(a + 1, b))):
        return ''
    elif s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]