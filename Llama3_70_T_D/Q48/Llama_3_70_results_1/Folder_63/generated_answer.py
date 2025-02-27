def return_binary_or_hexa(t):
    a = t[81]
    b = t[86]
    total = sum((i for i in range(a + 1, b) if i not in t[81:87]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]