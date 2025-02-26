def return_binary_or_hexa(tuple_input):
    a = tuple_input[77]
    b = tuple_input[84]
    excluded_range = set(tuple_input[77:85])
    sum_missing = sum((num for num in range(a + 1, b) if num not in excluded_range))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()