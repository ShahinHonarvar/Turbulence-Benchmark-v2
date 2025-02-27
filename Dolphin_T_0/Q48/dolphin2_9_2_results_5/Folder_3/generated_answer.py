def return_binary_or_hexa(int_tuples):
    a = int_tuples[56]
    b = int_tuples[88]
    int_set = set(int_tuples)
    sum_ints = sum((i for i in range(a + 1, b) if i not in int_set))
    if sum_ints % 2 != 0:
        return bin(sum_ints)[2:]
    else:
        return hex(sum_ints)[2:]