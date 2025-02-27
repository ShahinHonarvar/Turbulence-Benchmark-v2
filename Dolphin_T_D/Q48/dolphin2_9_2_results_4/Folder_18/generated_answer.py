def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    total = sum((a + 1 <= i <= b - 1 and i not in t for i in range(a + 1, b)))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]