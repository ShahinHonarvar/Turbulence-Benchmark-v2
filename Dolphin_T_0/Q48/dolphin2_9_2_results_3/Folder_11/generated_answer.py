def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    total = sum(set(range(a + 1, b)) - set(t[49:76]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()