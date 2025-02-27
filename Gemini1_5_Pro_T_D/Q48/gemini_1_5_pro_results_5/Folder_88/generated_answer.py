def return_binary_or_hexa(tuple1):
    a = tuple1[3]
    b = tuple1[9]
    sum = 0
    for i in range(a + 1, b):
        if i not in tuple1[3:10]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]