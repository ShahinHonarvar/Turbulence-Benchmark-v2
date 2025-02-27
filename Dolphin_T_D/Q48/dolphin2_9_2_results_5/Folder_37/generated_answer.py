def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[7]
    if all((x in tup for x in range(a + 1, b))):
        return ''
    else:
        sum_val = sum((x for x in range(a + 1, b) if x not in tup))
        if sum_val % 2 == 0:
            return hex(sum_val)[2:]
        else:
            return bin(sum_val)[2:]