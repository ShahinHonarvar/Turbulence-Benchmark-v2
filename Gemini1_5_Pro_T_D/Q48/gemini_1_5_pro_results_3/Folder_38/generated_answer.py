def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    sum_val = 0
    for num in range(a + 1, b):
        if num not in tup[36:86]:
            sum_val += num
    if sum_val == 0:
        return ''
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]