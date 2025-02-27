def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[36]
    b = tuple_of_integers[52]
    range_of_numbers = set(range(a + 1, b))
    numbers_in_tuple = set(tuple_of_integers[36:53])
    missing_numbers = sorted(list(range_of_numbers - numbers_in_tuple))
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:]