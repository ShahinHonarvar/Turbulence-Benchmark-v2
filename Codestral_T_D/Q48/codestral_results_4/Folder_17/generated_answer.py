def return_binary_or_hexa(tuple_input):
    a = tuple_input[73]
    b = tuple_input[84]
    range_list = set(range(a + 1, b))
    missing_numbers = range_list - set(tuple_input[73 + 1:84])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''