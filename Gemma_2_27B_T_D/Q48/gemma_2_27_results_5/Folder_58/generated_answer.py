def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[275:871]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]