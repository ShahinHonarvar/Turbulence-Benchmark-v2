def return_binary_or_hexa(numbers):
    if len(numbers) < 98:
        return ''
    a = numbers[90]
    b = numbers[97]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[91:97])
    missing_numbers = expected_set - actual_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]