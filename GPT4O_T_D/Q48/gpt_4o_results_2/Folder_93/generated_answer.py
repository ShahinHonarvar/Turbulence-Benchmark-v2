def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing_sum = 0
    numbers_set = set(numbers[58:85])
    for num in range(a + 1, b):
        if num not in numbers_set:
            missing_sum += num
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'X')
    else:
        return format(missing_sum, 'b')