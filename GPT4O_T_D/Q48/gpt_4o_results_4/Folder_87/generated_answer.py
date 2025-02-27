def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[21:43])
    missing_numbers_sum = sum(expected_set - actual_set)
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]