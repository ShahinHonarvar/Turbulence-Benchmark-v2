def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    s = sum((i for i in range(a + 1, b) if i not in t[1:5]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]