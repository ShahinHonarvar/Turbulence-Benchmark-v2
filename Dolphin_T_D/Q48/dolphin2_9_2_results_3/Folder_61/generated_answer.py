def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    present = set(t[1:9])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]