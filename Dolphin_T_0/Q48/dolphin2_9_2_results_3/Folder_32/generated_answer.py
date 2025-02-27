def return_binary_or_hexa(tuple_of_integers):
    if len(tuple_of_integers) < 90:
        return ''
    a = tuple_of_integers[86]
    b = tuple_of_integers[90]
    missing = [i for i in range(a + 1, b) if i not in tuple_of_integers]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]