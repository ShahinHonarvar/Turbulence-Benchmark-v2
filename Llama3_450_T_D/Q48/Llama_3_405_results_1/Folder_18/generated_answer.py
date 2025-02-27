def return_binary_or_hexa(t):
    a = t[56]
    b = t[90]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in t[57:90] if a < i < b))
    diff = expected_sum - actual_sum
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]