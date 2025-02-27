def return_binary_or_hexa(tupl):
    a, b = (tupl[20], tupl[200])
    present = set(tupl[20:201])
    total = sum((i for i in range(a + 1, b) if i not in present))
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]