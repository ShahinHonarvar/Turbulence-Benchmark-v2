def return_binary_or_hexa(numbers):
    if len(numbers) < 100:
        return ''
    a = numbers[68]
    b = numbers[99]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[69:100]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')