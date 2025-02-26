def return_binary_or_hexa(tuple_input):
    a = tuple_input[36]
    b = tuple_input[54]
    sum_range = set(range(a + 1, b))
    tuple_range = set(tuple_input[36:55])
    missing_nums = sum_range - tuple_range
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]