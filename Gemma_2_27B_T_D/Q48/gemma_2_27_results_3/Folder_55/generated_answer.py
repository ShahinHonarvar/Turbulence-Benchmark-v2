def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[10:12 + 1]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]