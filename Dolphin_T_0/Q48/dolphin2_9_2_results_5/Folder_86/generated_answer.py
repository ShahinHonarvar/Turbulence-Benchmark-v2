def return_binary_or_hexa(t):
    a, b = (t[19], t[32])
    present = set(t[20:32])
    total = sum(range(a + 1, b))
    missing = total - sum(present)
    if missing % 2 == 0:
        return hex(missing)[2:]
    else:
        return bin(missing)[2:]