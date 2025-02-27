def return_binary_or_hexa(tup):
    a = tup[40]
    b = tup[200]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[40:201]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()