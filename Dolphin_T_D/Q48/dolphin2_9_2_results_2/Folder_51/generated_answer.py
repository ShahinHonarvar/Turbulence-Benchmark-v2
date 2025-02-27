def return_binary_or_hexa(t):
    a = t[6]
    b = t[9]
    between = set(t[7:9])
    total = sum(set(range(a + 1, b)) - between)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper() if total > 0 else ''