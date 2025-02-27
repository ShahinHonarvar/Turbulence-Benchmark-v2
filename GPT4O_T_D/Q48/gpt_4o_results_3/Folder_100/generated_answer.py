def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    missing_sum = 0
    full_range_set = set(range(a + 1, b))
    numbers_set = set(numbers[45:78])
    missing_numbers = full_range_set - numbers_set
    if missing_numbers:
        missing_sum = sum(missing_numbers)
    else:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'X')
    else:
        return format(missing_sum, 'b')