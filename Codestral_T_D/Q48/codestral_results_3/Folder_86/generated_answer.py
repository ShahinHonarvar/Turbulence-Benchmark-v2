def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    s = sum((i for i in range(a + 1, b) if i not in tup[19:33]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]