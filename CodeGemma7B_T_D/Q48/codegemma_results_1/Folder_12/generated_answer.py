def return_binary_or_hexa(tup):
    a = tup[16]
    b = tup[87]
    sum = 0
    for num in range(a + 1, b):
        if num not in tup[16:88]:
            sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()