def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    expected_numbers = set(range(a + 1, b))
    actual_numbers = set(numbers[74:84])
    missing_numbers = expected_numbers - actual_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]