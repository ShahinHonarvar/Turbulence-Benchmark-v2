def return_binary_or_hexa(numbers):
    a_index = 57
    b_index = 84
    if len(numbers) <= b_index:
        return ''
    a = numbers[a_index]
    b = numbers[b_index]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[a_index + 1:b_index]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')