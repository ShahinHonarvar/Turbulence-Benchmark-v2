def return_binary_or_hexa(t):
    a = t[6]
    b = t[9]
    total = sum((i for i in range(a + 1, b) if i not in t[6:10]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()