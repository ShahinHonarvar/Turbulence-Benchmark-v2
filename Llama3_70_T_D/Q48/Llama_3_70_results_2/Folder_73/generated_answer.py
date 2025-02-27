def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[10]
    b = tuple_of_integers[76]
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in tuple_of_integers[10:77]))
    if sum_of_missing_numbers == 0:
        return ''
    if sum_of_missing_numbers % 2 == 1:
        return bin(sum_of_missing_numbers)[2:]
    return hex(sum_of_missing_numbers)[2:]