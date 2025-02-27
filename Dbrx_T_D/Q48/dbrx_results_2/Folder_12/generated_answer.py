def return_binary_or_hexa(nonnegative_int_tuple):
    a = nonnegative_int_tuple[16]
    b = nonnegative_int_tuple[87]
    sum_of_integers = sum(set(range(a + 1, b)) - set(nonnegative_int_tuple[16:88]))
    if sum_of_integers % 2 != 0:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()