def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    total = sum((x for x in range(a + 1, b) if x not in t[25:80]))
    return bin(total)[2:] if total % 2 else hex(total)[2:] if total else ''