def return_binary_or_hexa(t):
    a = t[70]
    b = t[200]
    excluded_set = set(t[70:201])
    sum_result = sum((x for x in range(a + 1, b) if x not in excluded_set))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].upper()