def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    res = sum(set(range(a + 1, b)) - set(tup[15:58]))
    return bin(res)[2:] if res & 1 else hex(res)[2:].upper()