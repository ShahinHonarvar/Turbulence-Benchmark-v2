def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[20]
    b = tuple_of_integers[200]
    missing_integers = [i for i in range(a + 1, b) if i not in tuple_of_integers]
    if len(missing_integers) == 0:
        return ''
    sum_of_integers = sum(missing_integers)
    if sum_of_integers % 2 != 0:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]