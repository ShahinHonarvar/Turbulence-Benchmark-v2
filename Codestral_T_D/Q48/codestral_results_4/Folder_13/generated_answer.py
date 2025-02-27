def return_binary_or_hexa(num_tuple):
    a = num_tuple[46]
    b = num_tuple[91]
    missing_nums = set(range(a + 1, b)) - set(num_tuple[46 + 1:91])
    missing_sum = sum(missing_nums)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]