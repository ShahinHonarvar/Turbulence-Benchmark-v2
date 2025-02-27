def return_binary_or_hexa(data):
    a = data[0]
    b = data[2]
    total = sum((i for i in range(a + 1, b) if i not in data[:3]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()