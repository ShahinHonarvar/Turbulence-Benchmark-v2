def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    range_set = set(range(a + 1, b))
    missing_set = range_set - set(tup[11:79])
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]