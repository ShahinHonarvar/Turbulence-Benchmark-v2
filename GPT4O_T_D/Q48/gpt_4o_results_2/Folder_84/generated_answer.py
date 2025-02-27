def return_binary_or_hexa(t):
    a = t[32]
    b = t[44]
    expected_set = set(range(a + 1, b))
    actual_set = set(t[33:44])
    missing_set = expected_set - actual_set
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]