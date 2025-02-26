def return_binary_or_hexa(tuple_input):
    a = tuple_input[29]
    b = tuple_input[53]
    range_set = set(tuple_input[29:54])
    missing_nums = [num for num in range(a + 1, b) if num not in range_set]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]