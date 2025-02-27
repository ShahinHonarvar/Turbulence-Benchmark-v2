def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    current_range_set = set(numbers[21:93])
    missing_sum = sum((x for x in range(a + 1, b) if x not in current_range_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')