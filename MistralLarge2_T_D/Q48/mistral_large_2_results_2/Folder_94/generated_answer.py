def return_binary_or_hexa(t):
    a, b = (t[42], t[87])
    s = sum(set(range(a + 1, b)) - set(t[42:88]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]