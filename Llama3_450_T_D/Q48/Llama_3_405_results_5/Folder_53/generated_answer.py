def return_binary_or_hexa(tup):
    a, b = (tup[200], tup[202])
    sum_val = sum((i for i in range(a + 1, b) if i not in tup[200:202]))
    if sum_val == 0:
        return ''
    return bin(sum_val)[2:] if sum_val % 2 else hex(sum_val)[2:]