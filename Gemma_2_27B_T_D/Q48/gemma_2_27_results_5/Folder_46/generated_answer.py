def return_binary_or_hexa(data):
    a = data[10]
    b = data[79]
    total = sum([i for i in range(a + 1, b) if i not in data[10:80]])
    return bin(total)[2:] if total % 2 else hex(total)[2:]