def return_binary_or_hexa(t):
    if len(t) < 85:
        return ''
    a = t[73]
    b = t[84]
    numbers_in_range = set(t[74:84])
    expected_numbers = set(range(a + 1, b))
    missing_numbers = expected_numbers - numbers_in_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]