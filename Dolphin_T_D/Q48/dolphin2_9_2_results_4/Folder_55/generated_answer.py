def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    present = set(t[10:13])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]