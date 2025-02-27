def return_binary_or_hexa(tup):
    a = tup[933]
    b = tup[996]
    numbers = (x for x in range(a + 1, b))
    tup_933_996 = (x for x in tup[933:997])
    sum = 0
    for num in numbers:
        if num not in tup_933_996:
            sum += num
    if sum % 2 == 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()