def return_binary_or_hexa(num_tuple):
    a = num_tuple[29]
    b = num_tuple[53]
    full_set = set(range(a + 1, b))
    present_set = set(num_tuple[30:54])
    missing_nums = full_set - present_set
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]