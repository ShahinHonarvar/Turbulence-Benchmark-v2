def return_binary_or_hexa(tuple_values):
    a = tuple_values[36]
    b = tuple_values[85]
    numbers_between_a_b = set(range(a + 1, b))
    indices_a_b = set(tuple_values[36:85])
    not_in_tuple = list(numbers_between_a_b.difference(indices_a_b))
    if not not_in_tuple:
        return ''
    sum_ = sum(not_in_tuple)
    if sum_ % 2 == 0:
        return hex(sum_)[2:].upper()
    else:
        return bin(sum_)[2:]