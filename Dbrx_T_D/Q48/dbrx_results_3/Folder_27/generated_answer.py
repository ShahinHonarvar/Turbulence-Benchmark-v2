def return_binary_or_hexa(tup):
    a, b = (tup[86], tup[89])
    sum = 0
    if a + 1 < b - 1:
        for i in range(a + 1, b):
            if i not in tup[a + 1:b - 1]:
                sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()