def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[78]
    sum = 0
    for i in range(a + 1, b):
        if tup[i] not in tup[44:79]:
            sum += tup[i]
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]