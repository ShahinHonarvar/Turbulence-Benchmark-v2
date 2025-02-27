def return_binary_or_hexa(integer_tuple):
    sum_of_missing_integers = 0
    for i in range(integer_tuple[20] + 1, integer_tuple[43]):
        if i not in integer_tuple[20:43]:
            sum_of_missing_integers += i
    if sum_of_missing_integers % 2 == 1:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:].upper()