def return_binary_or_hexa(tup):
    a = tup[29]
    b = tup[53]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[29:53]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]