def return_binary_or_hexa(tuple_input):
    a = tuple_input[86]
    b = tuple_input[89]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[86:90])
    missing_sum = sum(range_set - tuple_set)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].lstrip('0')