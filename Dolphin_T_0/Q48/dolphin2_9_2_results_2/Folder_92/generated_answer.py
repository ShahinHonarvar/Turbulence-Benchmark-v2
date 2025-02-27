def return_binary_or_hexa(data):
    a = data[0]
    b = data[2]
    result = sum((i for i in range(a + 1, b) if i not in data[1:2]))
    return bin(result)[2:] if result % 2 != 0 else hex(result)[2:] if result != 0 else ''