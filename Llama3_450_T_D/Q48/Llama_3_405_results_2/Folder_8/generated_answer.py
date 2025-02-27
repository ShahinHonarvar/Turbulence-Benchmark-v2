def return_binary_or_hexa(tup):
    a = tup[45]
    b = tup[48]
    missing_nums = set(range(a + 1, b)) - set(tup[46:48])
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]