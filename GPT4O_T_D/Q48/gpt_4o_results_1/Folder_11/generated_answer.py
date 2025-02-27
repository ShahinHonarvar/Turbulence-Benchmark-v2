def return_binary_or_hexa(numbers):
    if len(numbers) < 77:
        return ''
    a, b = (numbers[48], numbers[76])
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[49:76])
    missing_numbers = full_range - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')