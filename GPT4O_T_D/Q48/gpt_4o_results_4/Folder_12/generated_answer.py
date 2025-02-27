def return_binary_or_hexa(numbers):
    a, b = (numbers[16], numbers[87])
    missing_values = set(range(a + 1, b)).difference(numbers[17:87])
    if not missing_values:
        return ''
    total_sum = sum(missing_values)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')