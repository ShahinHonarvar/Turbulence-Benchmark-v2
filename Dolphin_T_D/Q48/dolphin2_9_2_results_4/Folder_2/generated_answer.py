def return_binary_or_hexa(t):
    a, b = (t[72], t[93])
    total = sum(set(range(a + 1, b)) - set(t[73:93]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]