def return_binary_or_hexa(tuple_of_integers):
    a, b = (tuple_of_integers[427], tuple_of_integers[669])
    sum_of_missing_numbers = sum((x for x in range(a + 1, b) if tuple_of_integers[427:669].count(x) == 0))
    if sum_of_missing_numbers % 2 != 0:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()