def return_binary_or_hexa(values):
    a, b = (values[50], values[92])
    total = sum((x for x in range(a + 1, b) if x not in values[50:93]))
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:].upper()