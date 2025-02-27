def return_binary_or_hexa(numbers):
    a = numbers[6]
    b = numbers[9]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[7:9])
    missing_numbers = expected_set - actual_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]