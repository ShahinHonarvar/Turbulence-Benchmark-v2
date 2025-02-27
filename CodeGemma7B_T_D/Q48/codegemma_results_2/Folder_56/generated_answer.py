def return_binary_or_hexa(values):
    a, b = (values[7], values[9])
    total = 0
    for i in range(a + 1, b):
        if i not in values[7:10]:
            total += i
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()