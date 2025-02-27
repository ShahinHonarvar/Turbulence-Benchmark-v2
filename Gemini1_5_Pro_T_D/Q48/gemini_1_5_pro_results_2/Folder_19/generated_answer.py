def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[1:5]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]