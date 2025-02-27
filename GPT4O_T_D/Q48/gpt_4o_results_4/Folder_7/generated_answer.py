def return_binary_or_hexa(numbers):
    if len(numbers) < 98:
        return ''
    a = numbers[10]
    b = numbers[97]
    expected_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[11:97])
    missing_numbers = expected_numbers - present_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]