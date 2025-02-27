def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[8]
    sum = 0
    for k in range(a + 1, b):
        if k not in tup[2:9]:
            sum += k
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()