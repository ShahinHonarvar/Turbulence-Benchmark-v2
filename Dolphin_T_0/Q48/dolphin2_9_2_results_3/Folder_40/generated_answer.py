def return_binary_or_hexa(t):
    a, _, _, b = t
    present = set(t[1:4])
    total = sum(range(a + 1, b)) - sum(present)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper() if total else ''