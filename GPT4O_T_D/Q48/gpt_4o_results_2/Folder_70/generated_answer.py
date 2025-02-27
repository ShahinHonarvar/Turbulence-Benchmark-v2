def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in numbers[44:70]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 0:
        return format(missing_numbers_sum, 'x')
    return format(missing_numbers_sum, 'b')