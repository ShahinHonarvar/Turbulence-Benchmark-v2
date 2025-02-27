def return_binary_or_hexa(numbers):
    if len(numbers) <= 100:
        return ''
    a = numbers[10]
    b = numbers[100]
    present_numbers = set(numbers[11:100])
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 0:
        return format(missing_numbers_sum, 'x')
    else:
        return format(missing_numbers_sum, 'b')