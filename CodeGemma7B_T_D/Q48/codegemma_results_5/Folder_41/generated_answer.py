def return_binary_or_hexa(tp):
    a, b = (tp[3], tp[8])
    if b < a:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in tp[3:9]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()