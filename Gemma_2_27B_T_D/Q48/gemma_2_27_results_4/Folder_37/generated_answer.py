def return_binary_or_hexa(data):
    a = data[2]
    b = data[7]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[2:8]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]