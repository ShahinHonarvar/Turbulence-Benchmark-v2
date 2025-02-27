def return_binary_or_hexa(tup):
    a = tup[200]
    b = tup[202]
    sum_val = sum((i for i in range(a + 1, b) if i not in tup[200:203]))
    if sum_val % 2 == 0:
        return hex(sum_val)[2:]
    return bin(sum_val)[2:]