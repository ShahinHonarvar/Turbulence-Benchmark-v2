def return_binary_or_hexa(data):
    a = data[69]
    b = data[97]
    total = sum((i for i in range(a + 1, b) if i not in data[69:98]))
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]