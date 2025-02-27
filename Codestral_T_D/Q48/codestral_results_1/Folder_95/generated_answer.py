def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[32]
    b = tuple_of_ints[99]
    sum_missing = sum((i for i in range(a + 1, b) if i not in tuple_of_ints[32:99]))
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]