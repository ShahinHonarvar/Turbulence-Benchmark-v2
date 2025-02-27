def return_binary_or_hexa(t):
    a, b = (t[7], t[9])
    missing = [x for x in range(a + 1, b) if x not in t]
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()