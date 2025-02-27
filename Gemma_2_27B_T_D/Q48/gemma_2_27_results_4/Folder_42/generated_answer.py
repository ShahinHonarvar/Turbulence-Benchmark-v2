def return_binary_or_hexa(t):
    a = t[18]
    b = t[60]
    total = sum((i for i in range(a + 1, b) if i not in t[18:60]))
    if total % 2 != 0:
        return bin(total)[2:]
    return hex(total)[2:].upper()