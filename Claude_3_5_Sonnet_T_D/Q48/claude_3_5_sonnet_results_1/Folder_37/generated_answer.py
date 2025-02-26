def return_binary_or_hexa(tuple_input):
    a = tuple_input[2]
    b = tuple_input[7]
    excluded_nums = set(tuple_input[2:8])
    sum_result = sum((num for num in range(a + 1, b) if num not in excluded_nums))
    if sum_result == 0:
        return ''
    elif sum_result % 2 != 0:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]