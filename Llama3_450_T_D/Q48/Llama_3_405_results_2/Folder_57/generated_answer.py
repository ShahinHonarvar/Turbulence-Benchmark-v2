def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    full_set = set(range(a + 1, b))
    tup_set = set(tup[26:80])
    diff_set = full_set - tup_set
    total_sum = sum(diff_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]