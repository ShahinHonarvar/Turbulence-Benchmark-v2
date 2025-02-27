def return_binary_or_hexa(data):
    a = data[18]
    b = data[60]
    total = 0
    for i in range(a + 1, b):
        if i not in data[18:60]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]