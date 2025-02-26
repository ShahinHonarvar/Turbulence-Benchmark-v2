def return_binary_or_hexa(tuple_input):
    a = tuple_input[33]
    b = tuple_input[78]
    set_range = set(range(a + 1, b))
    set_tuple = set(tuple_input[34:78])
    missing_sum = sum(set_range - set_tuple)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]