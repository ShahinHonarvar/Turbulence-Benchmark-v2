def return_binary_or_hexa(tuple_input):
    a = tuple_input[36]
    b = tuple_input[54]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[36:55])
    missing_sum = sum(range_set - tuple_set)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')