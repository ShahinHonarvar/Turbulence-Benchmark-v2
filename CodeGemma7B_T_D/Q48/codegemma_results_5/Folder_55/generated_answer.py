def return_binary_or_hexa(tup):
    a, b = (tup[10], tup[12])
    res = 0
    for i in range(a + 1, b):
        if i not in tup[10:13]:
            res += i
    if res % 2:
        return str(bin(res))[2:]
    else:
        return hex(res)[2:].upper()