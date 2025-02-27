def return_binary_or_hexa(numbers):
    if len(numbers) <= 90:
        return ''
    a = numbers[56]
    b = numbers[90]
    complete_set = set(range(a + 1, b))
    subset = set(numbers[57:90])
    missing_numbers = complete_set - subset
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')