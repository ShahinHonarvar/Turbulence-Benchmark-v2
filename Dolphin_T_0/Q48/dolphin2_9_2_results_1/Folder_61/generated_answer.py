def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum(t[1:9])
    if actual_sum == expected_sum:
        return ''
    elif actual_sum % 2:
        return bin(expected_sum)[2:]
    else:
        return hex(expected_sum)[2:]