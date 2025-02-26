def return_binary_or_hexa(tuple_input):
    a = tuple_input[110]
    b = tuple_input[348]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[110:349])
    missing_numbers = range_set - tuple_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]