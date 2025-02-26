def return_binary_or_hexa(tuple_input):
    a = tuple_input[86]
    b = tuple_input[99]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[87:99])
    missing_numbers = sum_range - sum_tuple
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')