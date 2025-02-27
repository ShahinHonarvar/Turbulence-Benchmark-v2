def return_binary_or_hexa(tpl):
    a = tpl[44]
    b = tpl[78]
    range_set = set(range(a + 1, b))
    tpl_set = set(tpl[45:78])
    missing_set = range_set - tpl_set
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]