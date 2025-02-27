def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[72]
    b = tuple_of_integers[93]
    missing_numbers = set(range(a + 1, b)) - set(tuple_of_integers[73:93])
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()