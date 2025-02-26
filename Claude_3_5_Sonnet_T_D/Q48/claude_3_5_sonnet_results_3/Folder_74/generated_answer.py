def return_binary_or_hexa(tuple_input):
    a = tuple_input[69]
    b = tuple_input[97]
    tuple_range = set(tuple_input[69:98])
    sum_total = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_total == 0:
        return ''
    elif sum_total % 2 != 0:
        return bin(sum_total)[2:]
    else:
        return hex(sum_total)[2:]