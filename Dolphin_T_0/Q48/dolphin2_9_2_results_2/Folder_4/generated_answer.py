def return_binary_or_hexa(t):
    a, b = (t[49], t[74])
    s = set(t)
    total = sum((x for x in range(a + 1, b) if x not in s))
    return bin(total)[2:] if total % 2 else hex(total)[2:]