def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[5])
    sum_of_absent = sum((i for i in range(a + 1, b) if i not in tup))
    if sum_of_absent == 0:
        return ''
    elif sum_of_absent % 2:
        return bin(sum_of_absent)[2:]
    else:
        return hex(sum_of_absent)[2:]