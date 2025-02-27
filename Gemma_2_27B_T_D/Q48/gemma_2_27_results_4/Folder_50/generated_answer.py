def return_binary_or_hexa(data):
    a = data[13]
    b = data[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[13:77]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    elif sum == 0:
        return ''
    else:
        return hex(sum)[2:]