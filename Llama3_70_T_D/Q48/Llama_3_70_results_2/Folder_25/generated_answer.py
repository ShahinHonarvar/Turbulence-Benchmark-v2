def return_binary_or_hexa(tup):
    a, b = (tup[37], tup[43])
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[37:44]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]