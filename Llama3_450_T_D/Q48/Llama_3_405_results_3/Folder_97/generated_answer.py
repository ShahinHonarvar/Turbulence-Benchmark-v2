def return_binary_or_hexa(tup):
    a = tup[34]
    b = tup[69]
    full_set = set(range(a + 1, b))
    tup_set = set(tup[35:69])
    diff_set = full_set - tup_set
    total_sum = sum(diff_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]