def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[10]
    full_range = set(range(a + 1, b))
    actual_range = set(tup[1:10])
    diff_range = full_range - actual_range
    total_sum = sum(diff_range)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]