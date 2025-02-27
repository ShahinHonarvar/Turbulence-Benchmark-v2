def return_binary_or_hexa(tuple_input):
    a = tuple_input[77]
    b = tuple_input[84]
    sum_missing = sum((i for i in range(a + 1, b) if i not in tuple_input[77:84]))
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]