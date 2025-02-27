def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[20]
    b = integer_tuple[43]
    if a + 1 > b - 1:
        return ''
    subarray_integers = integer_tuple[20:43]
    sum_of_integers = sum(range(a + 1, b)) - sum(subarray_integers)
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].upper()
    else:
        return bin(sum_of_integers)[2:]