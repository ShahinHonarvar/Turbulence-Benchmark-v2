def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[2]
    s = sum((i for i in range(a + 1, b) if i not in tup[1:2]))
    if s == 0 or all((i in tup[1:2] for i in range(a + 1, b))):
        return ''
    elif s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]