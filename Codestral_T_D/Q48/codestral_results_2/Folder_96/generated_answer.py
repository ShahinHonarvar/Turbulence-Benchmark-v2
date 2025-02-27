def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[200]
    s = sum((i for i in range(a + 1, b) if i not in tup[50:200]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''