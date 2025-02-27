def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[100]
    summ = sum((i for i in range(a + 1, b) if i not in tup[10:100]))
    if summ % 2:
        return bin(summ)[2:]
    else:
        return hex(summ)[2:].upper()