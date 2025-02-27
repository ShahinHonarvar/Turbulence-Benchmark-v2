def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    s = sum(set(range(a + 1, b)) - set(t[3:7]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]