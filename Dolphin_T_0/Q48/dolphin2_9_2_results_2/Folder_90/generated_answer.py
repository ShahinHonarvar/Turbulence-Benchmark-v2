def return_binary_or_hexa(t):
    a, b = (t[60], t[90])
    missing = [i for i in range(a + 1, b) if i not in t[61:90]]
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]