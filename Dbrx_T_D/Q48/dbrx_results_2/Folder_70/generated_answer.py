def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[69]
    missing_numbers = set(range(a + 1, b)) - set(numbers[43:70])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')