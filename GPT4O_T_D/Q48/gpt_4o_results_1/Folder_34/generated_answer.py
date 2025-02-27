def return_binary_or_hexa(numbers):
    if len(numbers) <= 200:
        return ''
    a = numbers[60]
    b = numbers[200]
    missing_sum = sum({i for i in range(a + 1, b)} - set(numbers[61:200]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')