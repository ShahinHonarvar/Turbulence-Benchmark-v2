def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    in_range_set = set(numbers[58:85])
    full_range_set = set(range(a + 1, b))
    missing_numbers = full_range_set - in_range_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')