def return_binary_or_hexa(data):
    a = data[57]
    b = data[84]
    total = sum((i for i in range(a + 1, b) if i not in data[57:85]))
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:].upper()