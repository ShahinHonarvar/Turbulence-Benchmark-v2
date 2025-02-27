def return_binary_or_hexa(data):
    a = data[933]
    b = data[996]
    total = 0
    for i in range(a + 1, b):
        if i not in data[933:997]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]