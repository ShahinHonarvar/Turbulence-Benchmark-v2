def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    missing = [x for x in range(a + 1, b) if x not in t[17:89]]
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]