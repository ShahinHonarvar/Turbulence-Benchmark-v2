def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[51]
    excluded_set = set(tuple_input[20:52])
    sum_total = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_total == 0:
        return ''
    if sum_total % 2 == 1:
        return bin(sum_total)[2:]
    else:
        return hex(sum_total)[2:]