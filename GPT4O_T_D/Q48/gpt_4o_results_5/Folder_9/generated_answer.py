def return_binary_or_hexa(numbers):
    if len(numbers) <= 200:
        return ''
    a = numbers[70]
    b = numbers[200]
    expected_numbers = set(range(a + 1, b))
    actual_numbers = set(numbers[71:200])
    missing_numbers = expected_numbers - actual_numbers
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]