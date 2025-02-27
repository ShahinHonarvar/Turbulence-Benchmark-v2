def return_binary_or_hexa(tuple_in):
    a = tuple_in[2]
    b = tuple_in[7]
    sum_val = sum(set(range(a + 1, b)) - set(tuple_in[2:8]))
    if sum_val % 2 != 0:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:]