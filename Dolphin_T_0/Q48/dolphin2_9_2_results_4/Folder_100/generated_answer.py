def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[44]
    b = tuple_of_integers[78]
    integers_between_a_b = set(range(a + 1, b))
    integers_in_tuple_between_a_b = set(tuple_of_integers[44:79])
    missing_integers_in_tuple = list(integers_between_a_b - integers_in_tuple_between_a_b)
    sum_of_missing_integers = sum(missing_integers_in_tuple)
    if sum_of_missing_integers % 2 == 0:
        return hex(sum_of_missing_integers)[2:]
    else:
        return bin(sum_of_missing_integers)[2:]