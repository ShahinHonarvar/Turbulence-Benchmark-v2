def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[93]
    full_set = set(range(a + 1, b))
    partial_set = set(tup[21:93])
    diff_set = full_set - partial_set
    total_sum = sum(diff_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]