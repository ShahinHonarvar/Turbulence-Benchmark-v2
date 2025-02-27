def return_binary_or_hexa(tup):
    a, b = (tup[37], tup[43])
    missing_nums = set(range(a + 1, b)) - set(tup[37 + 1:43])
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]