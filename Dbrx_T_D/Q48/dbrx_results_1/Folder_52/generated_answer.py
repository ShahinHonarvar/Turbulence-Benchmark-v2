def return_binary_or_hexa(tup):
    a, b = (tup[38], tup[81])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[38:82]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()