def return_binary_or_hexa(data):
    a = data[110]
    b = data[348]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[110:348]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]