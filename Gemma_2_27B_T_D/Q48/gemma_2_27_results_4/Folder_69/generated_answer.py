def return_binary_or_hexa(data):
    a = data[39]
    b = data[43]
    total = sum((i for i in range(a + 1, b) if i not in data[39:44]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()