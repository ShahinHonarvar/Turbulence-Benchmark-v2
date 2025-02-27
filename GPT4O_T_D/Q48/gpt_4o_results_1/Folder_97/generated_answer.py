def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    if a + 1 >= b:
        return ''
    all_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[35:69])
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')