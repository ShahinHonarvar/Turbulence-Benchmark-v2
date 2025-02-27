def return_binary_or_hexa(tup):
    a, b = (tup[25], tup[80])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[25:80]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]