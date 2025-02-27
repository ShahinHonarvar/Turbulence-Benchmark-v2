def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    range_numbers = set(range(a + 1, b))
    tuple_numbers = set(numbers[45:67])
    missing_numbers = range_numbers - tuple_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')