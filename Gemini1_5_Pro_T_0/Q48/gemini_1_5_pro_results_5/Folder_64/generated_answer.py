def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[5]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]