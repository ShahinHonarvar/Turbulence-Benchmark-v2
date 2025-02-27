def return_binary_or_hexa(t):
    a = t[44]
    b = t[91]
    full_range = set(range(a + 1, b))
    present_range = set(t[45:91])
    missing_numbers = full_range - present_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]