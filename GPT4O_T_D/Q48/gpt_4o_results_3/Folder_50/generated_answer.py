def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    missing_numbers_sum = sum((num for num in range(a + 1, b) if num not in numbers[14:76]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 0:
        return format(missing_numbers_sum, 'X').lstrip('0')
    else:
        return format(missing_numbers_sum, 'b').lstrip('0')