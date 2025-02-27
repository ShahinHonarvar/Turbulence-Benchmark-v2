def return_binary_or_hexa(tup):
    a, b = (tup[427], tup[669])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[427:670]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()