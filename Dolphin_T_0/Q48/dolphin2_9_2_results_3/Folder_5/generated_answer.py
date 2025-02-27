def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[2]
    b = tuple_of_integers[8]
    sum_integers = sum((i for i in range(a + 1, b) if i not in tuple_of_integers[3:9]))
    if sum_integers % 2 == 1:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:].upper()