def return_binary_or_hexa(tuple_input):
    a = tuple_input[38]
    b = tuple_input[81]
    missing = set(range(a + 1, b)) - set(tuple_input[39:81])
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]