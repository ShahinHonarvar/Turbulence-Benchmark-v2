def return_binary_or_hexa(num_tuple):
    a = num_tuple[29]
    b = num_tuple[53]
    expected_sum = b - 1 - (a + 1) + 1
    actual_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[30:53]))
    if actual_sum == expected_sum:
        return ''
    elif actual_sum % 2:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:]