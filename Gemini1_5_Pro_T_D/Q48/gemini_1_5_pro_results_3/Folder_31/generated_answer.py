def return_binary_or_hexa(tup):
    a = tup[33]
    b = tup[78]
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[34:78]:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]