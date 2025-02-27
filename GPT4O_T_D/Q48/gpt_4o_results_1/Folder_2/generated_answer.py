def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    required_numbers = set(range(a + 1, b))
    present_numbers = set(t[73:93])
    missing_numbers = required_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')