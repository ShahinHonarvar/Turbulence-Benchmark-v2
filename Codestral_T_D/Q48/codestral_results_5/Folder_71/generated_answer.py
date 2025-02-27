def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    range_set = set(t[20:36])
    sum_missing = sum((i for i in range(a + 1, b) if i not in range_set))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]