def return_binary_or_hexa(tup):
    a, b = (tup[57], tup[85])
    total = 0
    for i in range(a + 1, b):
        if i not in tup:
            total += i
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]