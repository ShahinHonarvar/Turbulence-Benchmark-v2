def return_binary_or_hexa(tup):
    a = tup[22]
    b = tup[24]
    result = 0
    for i in range(a + 1, b):
        if i not in tup[22:25]:
            result += i
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]