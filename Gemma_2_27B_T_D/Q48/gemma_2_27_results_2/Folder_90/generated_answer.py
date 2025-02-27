def return_binary_or_hexa(data):
    a = data[60]
    b = data[90]
    total = sum((x for x in range(a + 1, b) if x not in data[60:90]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]