def return_binary_or_hexa(tuple_input):
    a = tuple_input[62]
    b = tuple_input[96]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[62:97])
    missing_sum = sum(range_set - tuple_set)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]