def return_binary_or_hexa(data):
    a = data[25]
    b = data[80]
    total = 0
    for i in range(a + 1, b):
        if i not in data[25:81]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]