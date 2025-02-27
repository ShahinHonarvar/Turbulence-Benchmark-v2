def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[67]
    range_numbers = set(range(a + 1, b))
    tuple_subset = set(numbers[45:67])
    missing_numbers = range_numbers - tuple_subset
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 0:
        return format(sum_missing, 'x')
    else:
        return format(sum_missing, 'b')