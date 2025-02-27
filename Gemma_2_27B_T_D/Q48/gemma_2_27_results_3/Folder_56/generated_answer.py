def return_binary_or_hexa(data):
    a = data[7]
    b = data[9]
    total = sum((i for i in range(a + 1, b - 1 + 1) if i not in data[7:10]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]