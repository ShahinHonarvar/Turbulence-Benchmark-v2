def return_binary_or_hexa(data):
    a = data[20]
    b = data[51]
    total = sum((i for i in range(a + 1, b) if i not in data[20:51]))
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]