def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[8]
    sum_val = sum((i for i in range(a + 1, b) if i not in tup[1:9]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 != 0:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]