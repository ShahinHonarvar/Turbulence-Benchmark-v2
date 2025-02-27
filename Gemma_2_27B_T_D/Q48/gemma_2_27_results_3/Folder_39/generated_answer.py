def return_binary_or_hexa(data):
    a = data[44]
    b = data[91]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[44:92]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]