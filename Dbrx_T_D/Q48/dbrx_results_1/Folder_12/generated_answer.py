def return_binary_or_hexa(tup):
    a, b = (tup[16], tup[87])
    if a + 1 >= b - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[a + 1:b]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]