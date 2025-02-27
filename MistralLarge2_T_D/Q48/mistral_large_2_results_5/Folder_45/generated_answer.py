def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    s = sum(set(range(a + 1, b)) - set(t[30:201]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]