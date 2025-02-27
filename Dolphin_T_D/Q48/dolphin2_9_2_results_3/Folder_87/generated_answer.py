def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[20]
    b = tuple_of_integers[43]
    sum_integers = sum(range(a + 1, b)) - sum(tuple_of_integers[20:44])
    if sum_integers == 0:
        return ''
    elif sum_integers % 2 == 0:
        return hex(sum_integers)[2:].upper()
    else:
        return bin(sum_integers)[2:]