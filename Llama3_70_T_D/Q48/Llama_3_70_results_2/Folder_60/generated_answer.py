def return_binary_or_hexa(num_tuple):
    a = num_tuple[38]
    b = num_tuple[52]
    missing_nums = [x for x in range(a + 1, b) if x not in num_tuple[38:53]]
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''