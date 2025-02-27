def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[9])
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return format(sum_missing_numbers, '08b')
    else:
        return format(sum_missing_numbers, 'x')