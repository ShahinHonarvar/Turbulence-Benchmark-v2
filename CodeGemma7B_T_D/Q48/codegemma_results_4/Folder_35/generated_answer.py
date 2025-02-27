def return_binary_or_hexa(tup):
    sum = 0
    for i in range(85):
        if i < 77 or i > 84:
            sum += tup[i]
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()