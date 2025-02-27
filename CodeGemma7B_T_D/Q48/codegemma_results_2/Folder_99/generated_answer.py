def return_binary_or_hexa(tp):
    a, b = (tp[427], tp[669])
    sum = 0
    for i in range(a + 1, b):
        if i not in tp[427:670]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]