def return_binary_or_hexa(tup):
    a = tup[49]
    b = tup[74]
    sum = 0
    flag = 0
    for i in range(a + 1, b):
        if i not in tup:
            flag = flag ^ 1
            sum += i
    if flag == 0:
        return ''
    elif flag == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()