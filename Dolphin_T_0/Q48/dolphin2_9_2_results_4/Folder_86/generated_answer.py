def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    not_in_tup = [x for x in range(a + 1, b) if x not in tup[20:32]]
    sum_not_in_tup = sum(not_in_tup)
    if sum_not_in_tup % 2 != 0:
        return bin(sum_not_in_tup)[2:]
    else:
        return hex(sum_not_in_tup)[2:]