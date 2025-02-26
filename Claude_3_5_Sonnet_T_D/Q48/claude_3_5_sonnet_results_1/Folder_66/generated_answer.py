def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    range_set = set(t[11:77])
    sum_value = sum((x for x in range(a + 1, b) if x not in range_set))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]