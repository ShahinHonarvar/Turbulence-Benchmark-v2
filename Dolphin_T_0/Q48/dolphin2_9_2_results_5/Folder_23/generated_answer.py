def return_binary_or_hexa(distinct_integers):
    a = distinct_integers[20]
    b = distinct_integers[36]
    integer_range = list(range(a + 1, b))
    not_in_tuple = [i for i in integer_range if i not in distinct_integers[20:37]]
    sum_of_integers = sum(not_in_tuple)
    if sum_of_integers % 2 == 0:
        return hex(sum_of_integers)[2:].upper()
    else:
        return bin(sum_of_integers)[2:]