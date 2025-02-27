def return_binary_or_hexa(tup):
    sum = 0
    for i in range(tup[0] + 1, tup[3]):
        if i not in tup:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]