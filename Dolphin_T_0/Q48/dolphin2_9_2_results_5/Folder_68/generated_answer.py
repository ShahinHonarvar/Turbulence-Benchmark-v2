def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[0]
    b = tuple_of_integers[-1]
    missing_numbers = [i for i in range(a + 1, b) if i not in tuple_of_integers]
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]