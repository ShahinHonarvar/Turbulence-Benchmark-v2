def return_binary_or_hexa(t):
    a, b = (t[38], t[52])
    present = set(t[38:53])
    sum_missing = sum((i for i in range(a + 1, b) if i not in present))
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()