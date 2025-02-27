def return_binary_or_hexa(tup):
    a, b = (tup[16], tup[87])
    ls = tup[17:87] + tup[-1]
    if a + 1 < b:
        start, end = (a + 1, b - 1)
    else:
        start, end = (b - 1, a + 1)
    res = sum((n for n in range(start, end + 1) if n not in ls))
    return bin(res)[2:] if res % 2 else hex(res)[2:].upper()