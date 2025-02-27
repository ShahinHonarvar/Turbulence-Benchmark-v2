def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[60]
    b = tuple_of_integers[200]
    if all((i in tuple_of_integers for i in range(a + 1, b))):
        return ''
    sum_not_in_tuple = sum((i for i in range(a + 1, b) if i not in tuple_of_integers))
    if sum_not_in_tuple % 2 == 0:
        return hex(sum_not_in_tuple)[2:]
    else:
        return bin(sum_not_in_tuple)[2:]