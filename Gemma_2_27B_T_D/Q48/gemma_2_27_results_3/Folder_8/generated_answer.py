def return_binary_or_hexa(data):
    a = data[45]
    b = data[48]
    total = sum([i for i in range(a + 1, b) if i not in data[45:48]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()