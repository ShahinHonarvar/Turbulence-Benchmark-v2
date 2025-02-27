def return_binary_or_hexa(numbers):
    a, b = (numbers[36], numbers[85])
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[37:85])
    to_sum = missing_numbers - present_numbers
    total_sum = sum(to_sum)
    if not to_sum:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')