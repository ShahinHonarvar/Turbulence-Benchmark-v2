def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    full_range = set(range(a + 1, b))
    present_in_range = set(numbers[7:9])
    missing_numbers = full_range - present_in_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')