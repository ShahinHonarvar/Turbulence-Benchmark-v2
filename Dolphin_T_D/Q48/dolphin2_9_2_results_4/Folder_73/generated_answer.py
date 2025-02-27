def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[10]
    b = tuple_of_integers[76]
    sum_of_integers = sum(set(range(a + 1, b - 1)) - set(tuple_of_integers[11:76]))
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:]
    else:
        return bin(sum_of_integers)[2:]