def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[51]
    missing = [x for x in range(a + 1, b) if x not in input_tuple[21:51]]
    sum_ = sum(missing)
    if sum_ % 2 != 0:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]