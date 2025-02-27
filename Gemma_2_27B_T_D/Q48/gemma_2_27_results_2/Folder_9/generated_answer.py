def return_binary_or_hexa(data):
    a = data[70]
    b = data[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in data[70:201]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]