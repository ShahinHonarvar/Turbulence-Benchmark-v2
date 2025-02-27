def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    present = set(t[25:81])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]