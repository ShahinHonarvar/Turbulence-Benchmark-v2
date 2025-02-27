def return_binary_or_hexa(t):
    a = t[55]
    b = t[84]
    total = sum(set(range(a + 1, b)) - set(t[55:85]))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]