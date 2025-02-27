def return_binary_or_hexa(t):
    a = t[20]
    b = t[51]
    s = set(t[20:52])
    total = sum((x for x in range(a + 1, b) if x not in s))
    if not total:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]