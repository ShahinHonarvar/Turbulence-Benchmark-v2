def return_binary_or_hexa(tup):
    a = tup[55]
    b = tup[84]
    full_set = set(range(a + 1, b))
    actual_set = set(tup[56:84])
    diff_set = full_set - actual_set
    total_sum = sum(diff_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]