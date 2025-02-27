def return_binary_or_hexa(numbers):
    if len(numbers) <= 200:
        return ''
    a, b = (numbers[70], numbers[200])
    required_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[71:200])
    missing_numbers = required_numbers - present_numbers
    total_sum = sum(missing_numbers)
    if missing_numbers:
        if total_sum % 2 == 0:
            return format(total_sum, 'x').lstrip('0')
        else:
            return format(total_sum, 'b').lstrip('0')
    return ''