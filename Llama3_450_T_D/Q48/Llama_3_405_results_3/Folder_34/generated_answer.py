def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t[61:200]))
    sum_missing = expected_sum - actual_sum
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]