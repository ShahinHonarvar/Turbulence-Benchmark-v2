def return_binary_or_hexa(tup):
    l, r = (tup[45] + 1, tup[48])
    res = 0
    for i in range(l, r + 1):
        if i not in tup[45:49]:
            res += i
    if res % 2:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()