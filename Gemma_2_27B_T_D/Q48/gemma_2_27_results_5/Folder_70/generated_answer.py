def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    total = sum((i for i in range(a + 1, b) if i not in t[43:70]))
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]