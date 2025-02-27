def return_binary_or_hexa(tup):
    a = tup[22]
    b = tup[24]
    total = sum((val for val in range(a + 1, b) if val not in tup))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]