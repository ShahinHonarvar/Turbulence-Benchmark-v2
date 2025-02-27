def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    required_set = set(range(a + 1, b))
    existing_set = set(numbers[51:200])
    missing_set = required_set - existing_set
    if not missing_set:
        return ''
    total_sum = sum(missing_set)
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')