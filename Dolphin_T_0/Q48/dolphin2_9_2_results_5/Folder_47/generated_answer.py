def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    present = set(t[30:53] + [a, b])
    total = sum(set(range(a + 1, b)) - present)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]