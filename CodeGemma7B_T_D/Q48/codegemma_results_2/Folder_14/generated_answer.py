def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[5])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[2:6]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()