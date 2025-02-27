def return_binary_or_hexa(numbers):
    if len(numbers) < 8:
        return ''
    a = numbers[6]
    b = numbers[7]
    required_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[6:8])
    missing_numbers = required_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]