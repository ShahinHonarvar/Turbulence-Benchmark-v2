def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[52]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[36:53]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()