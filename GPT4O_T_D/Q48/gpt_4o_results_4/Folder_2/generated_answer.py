def return_binary_or_hexa(numbers):
    if len(numbers) <= 93:
        return ''
    a = numbers[72]
    b = numbers[93]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[73:93]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')