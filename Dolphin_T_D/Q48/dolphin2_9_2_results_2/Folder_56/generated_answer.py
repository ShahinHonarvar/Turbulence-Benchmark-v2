def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[7]
    b = tuple_of_ints[9]
    sum_of_integers = sum(set(range(a + 1, b)) - set(tuple_of_ints[7:10]))
    if sum_of_integers % 2:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]