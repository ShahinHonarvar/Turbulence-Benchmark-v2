def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[76]
    expected_sum = (b - a - 1) * (b + a) // 2
    actual_sum = sum((num for num in range(a + 1, b) if num not in tup[13:76]))
    total_sum = expected_sum - actual_sum
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]