def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[8])
    sum_not_in_tup = sum((i for i in range(a + 1, b) if i not in tup))
    if sum_not_in_tup % 2:
        return bin(sum_not_in_tup)[2:]
    else:
        return hex(sum_not_in_tup)[2:].upper()