def return_binary_or_hexa(data):
    a = data[0]
    b = data[4]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[:5]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()