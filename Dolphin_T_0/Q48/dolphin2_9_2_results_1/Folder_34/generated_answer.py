def return_binary_or_hexa(tup):
    a = tup[60]
    b = tup[200]
    s = 0
    for i in range(a + 1, b):
        if i not in tup:
            s += i
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]