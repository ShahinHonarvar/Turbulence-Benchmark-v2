def return_binary_or_hexa(numbers):
    if len(numbers) < 29:
        return ''
    a = numbers[10]
    b = numbers[28]
    expected_numbers = set(range(a + 1, b))
    actual_numbers = set(numbers[11:28])
    missing_numbers = expected_numbers - actual_numbers
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]