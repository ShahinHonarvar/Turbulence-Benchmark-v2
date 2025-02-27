def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[5])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[0:6]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]