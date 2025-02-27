def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[29]
    b = tuple_of_integers[53]
    missing_integers = [i for i in range(a + 1, b) if i not in tuple_of_integers[29:54]]
    sum_of_missing = sum(missing_integers)
    if sum_of_missing % 2 != 0:
        return bin(sum_of_missing)[2:]
    elif sum_of_missing != 0:
        return hex(sum_of_missing)[2:]
    else:
        return ''