def return_binary_or_hexa(t):
    a = t[44]
    b = t[67]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((i for i in t[45:67] if a < i < b))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]