def return_binary_or_hexa(data):
    a = data[10]
    b = data[28]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[10:29]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    elif sum != 0:
        return hex(sum)[2:]
    else:
        return ''