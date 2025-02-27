def return_binary_or_hexa(data):
    a = data[49]
    b = data[74]
    total = 0
    for i in range(a + 1, b):
        if i not in data[49:74]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]