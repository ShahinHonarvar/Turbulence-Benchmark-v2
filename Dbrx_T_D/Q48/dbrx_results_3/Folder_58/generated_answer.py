def return_binary_or_hexa(numbers):
    a, b = (numbers[275], numbers[871])
    missing_numbers = set(range(a + 1, b)) - set(numbers[276:871])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')