def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[49]
    b = tuple_of_integers[74]
    present_set = set(tuple_of_integers[50:74])
    missing_numbers = set(range(a + 1, b)) - present_set
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()