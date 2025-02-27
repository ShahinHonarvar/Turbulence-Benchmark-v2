def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[77]
    b = tuple_of_integers[84]
    sum_integers = sum(set(range(a + 1, b)) - set(tuple_of_integers[77:85]))
    return bin(sum_integers)[2:] if sum_integers % 2 else hex(sum_integers)[2:] if sum_integers != 0 else ''