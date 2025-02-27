def return_binary_or_hexa(t):
    a = t[39]
    b = t[43]
    expected_numbers = set(range(a + 1, b))
    existing_numbers = set(t[40:43])
    missing_numbers = expected_numbers - existing_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]