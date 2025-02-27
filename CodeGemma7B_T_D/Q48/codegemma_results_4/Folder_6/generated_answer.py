def return_binary_or_hexa(tup):
    sum = 0
    for i in range(tup[20] + 1, tup[93]):
        if i not in tup[20:94]:
            sum += i
    if sum % 2 == 1:
        return str(bin(sum))[2:]
    else:
        return str(hex(sum))[2:].upper()