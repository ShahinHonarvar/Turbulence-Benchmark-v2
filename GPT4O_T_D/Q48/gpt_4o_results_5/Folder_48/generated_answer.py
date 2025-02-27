def return_binary_or_hexa(lst):
    a = lst[933]
    b = lst[996]
    required_numbers = set(range(a + 1, b))
    present_numbers = set(lst[934:996])
    missing_numbers = required_numbers - present_numbers
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')