def return_binary_or_hexa(data):
    a = data[1]
    b = data[8]
    total = sum((i for i in range(a + 1, b) if i not in data[1:9]))
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()