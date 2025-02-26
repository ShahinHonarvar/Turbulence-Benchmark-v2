def return_binary_or_hexa(t):
    a = t[10]
    b = t[28]
    excluded_set = set(t[10:29])
    sum_range = sum((x for x in range(a + 1, b) if x not in excluded_set))
    if sum_range == 0:
        return ''
    elif sum_range % 2 != 0:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]