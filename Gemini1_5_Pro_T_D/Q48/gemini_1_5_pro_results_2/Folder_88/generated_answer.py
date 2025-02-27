def return_binary_or_hexa(tup):
    a = tup[3]
    b = tup[9]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[3:10]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]