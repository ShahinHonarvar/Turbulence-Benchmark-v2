def return_binary_or_hexa(tuple_input):
    a = tuple_input[38]
    b = tuple_input[52]
    range_tuple = tuple_input[38 + 1:52]
    missing_numbers = set(range(a + 1, b)) - set(range_tuple)
    sum_missing = sum(missing_numbers)
    if len(missing_numbers) == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]