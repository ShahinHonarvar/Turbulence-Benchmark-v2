def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    present = set(t[1:5])
    total = sum((x for x in range(a + 1, b) if x not in present))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]