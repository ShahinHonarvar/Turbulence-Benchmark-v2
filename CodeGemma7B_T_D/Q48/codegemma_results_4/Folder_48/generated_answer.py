def return_binary_or_hexa(tup):
    sum = 0
    for i in range(tup[933] + 1, tup[996]):
        if i not in tup[933:997]:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()