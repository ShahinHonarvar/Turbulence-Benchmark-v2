def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[55]
    b = tuple_of_integers[84]
    sum_of_missing_numbers = sum(set(range(a + 1, b)) - set(tuple_of_integers[55:85]))
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()