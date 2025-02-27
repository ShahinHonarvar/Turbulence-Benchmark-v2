def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[20:44]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]