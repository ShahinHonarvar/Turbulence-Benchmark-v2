def return_binary_or_hexa(t):
    a, b = (t[90], t[200])
    present = set((t[i] for i in range(90, 201)))
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]