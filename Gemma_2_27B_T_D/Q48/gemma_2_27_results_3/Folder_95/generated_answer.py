def return_binary_or_hexa(data):
    a = data[32]
    b = data[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[32:99]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]