def return_binary_or_hexa(tup):
    a = tup[43]
    b = tup[70]
    sum_val = sum((i for i in range(a + 1, b) if i not in tup[43:71]))
    if sum_val == 0:
        return ''
    if sum_val % 2 != 0:
        return bin(sum_val)[2:]
    return hex(sum_val)[2:]