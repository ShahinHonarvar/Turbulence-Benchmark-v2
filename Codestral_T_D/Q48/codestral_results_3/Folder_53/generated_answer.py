def return_binary_or_hexa(tuple_data):
    a = tuple_data[200]
    b = tuple_data[202]
    missing_numbers = set(range(a + 1, b)) - set(tuple_data[200:203])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''