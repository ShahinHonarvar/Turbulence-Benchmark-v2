def return_binary_or_hexa(numbers):
    a_index, b_index = (19, 32)
    a, b = (numbers[a_index], numbers[b_index])
    full_range = set(range(a + 1, b))
    present_range = set(numbers[a_index + 1:b_index])
    missing_numbers = sorted(full_range - present_range)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return f'{total_sum:x}'.lstrip('0') or '0'
    else:
        return f'{total_sum:b}'