def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in numbers[37:54]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return format(missing_numbers_sum, 'b')
    else:
        return format(missing_numbers_sum, 'x')