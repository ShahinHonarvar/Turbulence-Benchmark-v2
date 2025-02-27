def return_binary_or_hexa(num_tuple):
    a = num_tuple[3]
    b = num_tuple[9]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[3:9])
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]