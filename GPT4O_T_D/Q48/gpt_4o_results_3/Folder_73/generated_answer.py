def return_binary_or_hexa(numbers):
    if len(numbers) < 77:
        return ''
    a, b = (numbers[10], numbers[76])
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[11:76]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')