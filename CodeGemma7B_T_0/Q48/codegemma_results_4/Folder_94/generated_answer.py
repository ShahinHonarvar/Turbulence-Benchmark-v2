def return_binary_or_hexa(tup):
    a = tup[42]
    b = tup[87]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[42:88]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]