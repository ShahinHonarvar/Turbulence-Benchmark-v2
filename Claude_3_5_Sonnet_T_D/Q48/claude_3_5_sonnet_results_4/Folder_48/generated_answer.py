def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    range_set = set(t[933:997])
    sum_not_present = sum((x for x in range(a + 1, b) if x not in range_set))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]