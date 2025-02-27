def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in range(a + 1, b) if i not in t[58:85]))
    diff = expected_sum - actual_sum
    if diff == 0:
        return ''
    elif diff % 2 == 0:
        return hex(diff)[2:]
    else:
        return bin(diff)[2:]