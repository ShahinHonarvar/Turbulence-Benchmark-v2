def return_binary_or_hexa(tuple_input):
    a = tuple_input[36]
    b = tuple_input[52]
    excluded_set = set(tuple_input[36:53])
    sum_excluded = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_excluded == 0:
        return ''
    if sum_excluded % 2 == 1:
        return bin(sum_excluded)[2:]
    else:
        return hex(sum_excluded)[2:]