def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    expected_numbers = set(range(a + 1, b))
    actual_numbers = set(numbers[11:76])
    missing_numbers = expected_numbers - actual_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]