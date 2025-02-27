def return_binary_or_hexa(t):
    a, b = (t[81], t[86])
    total = sum(set(range(a + 1, b)) - set(t[82:86]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()