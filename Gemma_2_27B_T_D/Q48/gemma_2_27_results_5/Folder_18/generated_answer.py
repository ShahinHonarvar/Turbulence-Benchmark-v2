def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    total = sum([i for i in range(a + 1, b) if i not in t[56:90]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()