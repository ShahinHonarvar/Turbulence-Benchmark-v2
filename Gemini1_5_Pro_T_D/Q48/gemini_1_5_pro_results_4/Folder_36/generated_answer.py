def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[110:348]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]