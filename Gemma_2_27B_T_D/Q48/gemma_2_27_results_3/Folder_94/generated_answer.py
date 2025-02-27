def return_binary_or_hexa(data):
    a = data[42]
    b = data[87]
    total = sum((i for i in range(a + 1, b) if i not in data[42:87 + 1]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]