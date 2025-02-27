def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[68]
    b = tuple_of_integers[99]
    sum_of_missing_integers = sum((i for i in range(a + 1, b) if i not in tuple_of_integers[68:99]))
    if sum_of_missing_integers == 0:
        return ''
    elif sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]