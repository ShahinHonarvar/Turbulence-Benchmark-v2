def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[44]
    b = tuple_of_integers[67]
    sum_integers = 0
    range_integers = list(range(a + 1, b - 1))
    for i in tuple_of_integers:
        if i in range_integers:
            range_integers.remove(i)
    if not range_integers:
        return ''
    sum_integers = sum(range_integers)
    if sum_integers % 2 == 0:
        return hex(sum_integers)[2:].upper()
    else:
        return bin(sum_integers)[2:]