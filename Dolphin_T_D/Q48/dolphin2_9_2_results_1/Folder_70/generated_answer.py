def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    existing = {x for x in t[43:70]}
    total = sum((x for x in range(a + 1, b) if x not in existing))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]