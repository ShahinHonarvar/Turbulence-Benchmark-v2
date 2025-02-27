def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    s = sum((i for i in range(a + 1, b) if i not in tup[275:871]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]