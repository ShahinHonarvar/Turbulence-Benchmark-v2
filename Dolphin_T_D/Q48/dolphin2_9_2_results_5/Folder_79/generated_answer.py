def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    s = sum(range(a + 1, b))
    for i in range(2, 7):
        s -= t[i]
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]