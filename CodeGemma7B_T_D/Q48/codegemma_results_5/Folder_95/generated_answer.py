def return_binary_or_hexa(tup):
    lim = tup[99]
    res = 0
    for i in range(tup[32] + 1, lim):
        if i not in tup:
            res += i
    if res & 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()