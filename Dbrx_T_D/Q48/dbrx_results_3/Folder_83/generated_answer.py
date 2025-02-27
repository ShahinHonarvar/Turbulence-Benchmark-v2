def return_binary_or_hexa(numbers):
    a, b = (numbers[90], numbers[200])
    missing_numbers = set(range(a + 1, b)) - set(numbers[90:201])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return format(sum_missing, '08b')
    else:
        return format(sum_missing, '02x').upper()