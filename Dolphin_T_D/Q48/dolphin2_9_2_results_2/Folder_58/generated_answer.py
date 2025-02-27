def return_binary_or_hexa(t):
    a = t[275]
    b = t[871]
    total = sum((i for i in range(a + 1, b) if i not in t))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]