def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    total = sum((i for i in range(a + 1, b) if i not in t[39:44]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]