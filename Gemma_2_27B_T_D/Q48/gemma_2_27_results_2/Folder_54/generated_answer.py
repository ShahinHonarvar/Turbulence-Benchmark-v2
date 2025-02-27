def return_binary_or_hexa(data):
    a = data[35]
    b = data[64]
    total = sum((i for i in range(a + 1, b) if i not in data[35:64]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]