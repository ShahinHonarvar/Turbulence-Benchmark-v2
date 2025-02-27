def return_binary_or_hexa(tup):
    a, b = (tup[80], tup[200])
    full_set = set(range(a + 1, b))
    tup_set = set(tup[81:201])
    res = sum(full_set - tup_set)
    if not res:
        return ''
    return bin(res)[2:] if res & 1 else hex(res)[2:]