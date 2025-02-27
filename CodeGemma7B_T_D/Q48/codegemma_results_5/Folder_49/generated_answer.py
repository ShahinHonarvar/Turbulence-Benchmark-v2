def return_binary_or_hexa(tup):
    a = tup[80]
    b = tup[200]
    summ = 0
    for num in range(a + 1, b):
        if num not in tup[80:201]:
            summ += num
    if summ % 2 == 0:
        return hex(summ)[2:].upper()
    return bin(summ)[2:]