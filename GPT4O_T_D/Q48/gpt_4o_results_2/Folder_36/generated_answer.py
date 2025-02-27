def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[111:348])
    missing_numbers = full_range - present_numbers
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 0:
        return f'{total_sum:x}'
    else:
        return f'{total_sum:b}'