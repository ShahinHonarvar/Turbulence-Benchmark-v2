def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    missing = set(range(a + 1, b)) - set(t[1:8])
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]