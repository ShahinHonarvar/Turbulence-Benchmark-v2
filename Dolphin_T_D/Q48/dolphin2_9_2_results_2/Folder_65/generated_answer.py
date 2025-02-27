def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    present = set(t[51:76])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 1:
        return bin(total).replace('0b', '')
    else:
        return hex(total).replace('0x', '')