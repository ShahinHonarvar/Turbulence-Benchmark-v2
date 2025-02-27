def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    s = sum((i for i in range(a + 1, b) if i not in tup[13:36]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]