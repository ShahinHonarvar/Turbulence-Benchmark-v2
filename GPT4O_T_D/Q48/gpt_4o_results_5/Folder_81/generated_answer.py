def return_binary_or_hexa(numbers):
    if len(numbers) <= 100:
        return ''
    a = numbers[10]
    b = numbers[100]
    expected_set = set(range(a + 1, b))
    actual_set = set(numbers[11:100])
    missing_numbers = expected_set - actual_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]