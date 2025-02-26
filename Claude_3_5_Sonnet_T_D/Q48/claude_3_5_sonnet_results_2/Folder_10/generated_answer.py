def return_binary_or_hexa(tuple_input):
    a = tuple_input[36]
    b = tuple_input[54]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[36:55])
    missing_numbers = sum_range - sum_tuple
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]