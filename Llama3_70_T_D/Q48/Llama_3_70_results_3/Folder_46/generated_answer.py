def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    sum_val = sum((i for i in range(a + 1, b) if i not in tup[10:80]))
    if sum_val == 0:
        return ''
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    return hex(sum_val)[2:]