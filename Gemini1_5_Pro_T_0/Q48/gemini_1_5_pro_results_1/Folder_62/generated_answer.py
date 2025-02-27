def return_binary_or_hexa(tuple1):
    a = tuple1[50]
    b = tuple1[92]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple1[51:92]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]