def return_binary_or_hexa(t):
    a = t[50]
    b = t[92]
    expected_set = set(range(a + 1, b))
    actual_set = set(t[51:92])
    missing_numbers = expected_set - actual_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return f'{total_sum:x}'
    else:
        return f'{total_sum:b}'