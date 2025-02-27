def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    total = sum(range(a + 1, b)) - sum(t[57:90])
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]