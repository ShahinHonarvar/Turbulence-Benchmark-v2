def return_binary_or_hexa(t):
    a, b = (t[3], t[9])
    s = sum(set(range(a + 1, b)) - set(t[3:10]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]