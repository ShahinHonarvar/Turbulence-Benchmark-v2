def return_binary_or_hexa(data):
    a = data[1]
    b = data[4]
    total = sum((i for i in range(a + 1, b) if i not in data[1:5]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]