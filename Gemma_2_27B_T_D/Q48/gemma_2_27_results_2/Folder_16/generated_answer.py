def return_binary_or_hexa(data):
    a = data[90]
    b = data[97]
    total = sum((i for i in range(a + 1, b) if i not in data[90:98]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]