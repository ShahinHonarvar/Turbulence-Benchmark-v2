def return_binary_or_hexa(tuple_input):
    a = tuple_input[69]
    b = tuple_input[97]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[69:98])
    missing_sum = sum(sum_range - sum_tuple)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]