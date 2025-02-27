def return_binary_or_hexa(data):
    a = data[427]
    b = data[669]
    total = sum((i for i in range(a + 1, b) if i not in data[427:669]))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]