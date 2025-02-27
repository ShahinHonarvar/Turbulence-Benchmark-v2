def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[8])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[1:9]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()