def return_binary_or_hexa(tup):
    a, b = (tup[16], tup[87])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[16:88]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()