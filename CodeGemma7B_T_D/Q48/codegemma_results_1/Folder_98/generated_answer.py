def return_binary_or_hexa(arg):
    a, b = (arg[6], arg[7])
    seen = set(arg[6:8])
    res = sum((x for x in range(a + 1, b) if x not in seen))
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()