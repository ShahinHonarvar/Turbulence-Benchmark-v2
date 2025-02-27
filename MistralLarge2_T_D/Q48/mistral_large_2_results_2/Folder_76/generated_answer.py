def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    range_set = set(t[450:906])
    sum_missing = sum((x for x in range(a + 1, b) if x not in range_set))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]