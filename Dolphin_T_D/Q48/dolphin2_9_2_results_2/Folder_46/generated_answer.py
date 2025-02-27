def return_binary_or_hexa(t):
    a = t[10]
    b = t[79]
    present = set(t[11:79])
    total = sum(set(range(a + 1, b)) - present)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()