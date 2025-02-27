def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[85]
    full_range = set(range(a + 1, b))
    numbers_range = set(numbers[37:85])
    missing_numbers = full_range - numbers_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')