def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[60]
    b = tuple_of_integers[90]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers[60:91]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:].upper()
    else:
        return bin(sum_of_missing_numbers)[2:]