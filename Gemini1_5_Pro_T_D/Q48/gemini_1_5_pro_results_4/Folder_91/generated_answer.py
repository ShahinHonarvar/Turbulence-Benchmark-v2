def return_binary_or_hexa(tuple1):
    a = tuple1[0]
    b = tuple1[6]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple1:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]