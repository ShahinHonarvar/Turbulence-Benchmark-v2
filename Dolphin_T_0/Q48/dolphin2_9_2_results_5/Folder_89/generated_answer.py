def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    present = set(t[55:85])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].lower()