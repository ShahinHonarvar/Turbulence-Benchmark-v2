def return_binary_or_hexa(numbers):
    if len(numbers) < 100:
        return ''
    a = numbers[68]
    b = numbers[99]
    numbers_in_range = set(numbers[69:100])
    target_range = set(range(a + 1, b))
    missing_numbers = target_range - numbers_in_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')