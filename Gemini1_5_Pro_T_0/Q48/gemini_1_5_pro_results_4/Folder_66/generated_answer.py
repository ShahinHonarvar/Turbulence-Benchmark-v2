def return_binary_or_hexa(tuple1):
    a = tuple1[11]
    b = tuple1[76]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple1[11:77]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]