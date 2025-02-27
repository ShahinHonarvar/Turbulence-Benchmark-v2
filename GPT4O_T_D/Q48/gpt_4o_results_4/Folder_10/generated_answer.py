def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    full_range_set = set(range(a + 1, b))
    existing_numbers_set = set(numbers[37:54])
    missing_numbers_set = full_range_set - existing_numbers_set
    if not missing_numbers_set:
        return ''
    total_sum = sum(missing_numbers_set)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    return format(total_sum, 'b')