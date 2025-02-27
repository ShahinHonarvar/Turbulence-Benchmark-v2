def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[16]
    b = tuple_of_integers[87]
    sum_of_numbers = 0
    for i in range(a + 1, b):
        if i not in tuple_of_integers[17:87]:
            sum_of_numbers += i
    if sum_of_numbers == 0:
        return ''
    if sum_of_numbers % 2 == 1:
        return bin(sum_of_numbers)[2:]
    else:
        return hex(sum_of_numbers)[2:]