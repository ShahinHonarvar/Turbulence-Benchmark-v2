def return_binary_or_hexa(tup):
    sum = 0
    for i in range(tup[10] + 1, tup[100]):
        if i not in tup[10:100]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()