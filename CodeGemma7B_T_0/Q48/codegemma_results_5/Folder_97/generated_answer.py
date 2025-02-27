def return_binary_or_hexa(tup):
    a = tup[34]
    b = tup[69]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[34:69]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()