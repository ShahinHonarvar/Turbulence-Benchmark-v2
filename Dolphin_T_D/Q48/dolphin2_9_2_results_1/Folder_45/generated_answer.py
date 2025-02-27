def return_binary_or_hexa(tuple_integers):
    a = tuple_integers[30]
    b = tuple_integers[200]
    sum_integers = sum(set(range(a + 1, b)) - set(tuple_integers[31:200]))
    if sum_integers % 2 == 1:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:]