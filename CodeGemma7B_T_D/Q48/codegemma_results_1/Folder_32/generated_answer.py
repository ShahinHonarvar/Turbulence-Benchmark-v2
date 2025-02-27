def return_binary_or_hexa(tup):
    ex_tup2 = set(range(tup[86] + 1, tup[90])) - set(tup[86:90])
    if sum(ex_tup2) % 2:
        return bin(sum(ex_tup2))[2:]
    else:
        return hex(sum(ex_tup2))[2:].upper()