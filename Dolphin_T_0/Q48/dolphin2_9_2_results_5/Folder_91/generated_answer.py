def return_binary_or_hexa(t):
    a = t[0]
    b = t[6]
    s = sum(range(a + 1, b)) - sum(t[1:6])
    if s == 0:
        return ''
    elif s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]