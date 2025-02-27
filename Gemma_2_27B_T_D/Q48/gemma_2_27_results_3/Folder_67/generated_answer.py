def return_binary_or_hexa(data):
    a = data[44]
    b = data[67]
    total = sum([i for i in range(a + 1, b) if i not in data[44:67]])
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()