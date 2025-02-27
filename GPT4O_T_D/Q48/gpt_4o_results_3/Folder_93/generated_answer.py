def return_binary_or_hexa(t):
    a = t[57]
    b = t[85]
    expected_numbers = set(range(a + 1, b))
    present_numbers = set(t[58:85])
    missing_numbers = expected_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')