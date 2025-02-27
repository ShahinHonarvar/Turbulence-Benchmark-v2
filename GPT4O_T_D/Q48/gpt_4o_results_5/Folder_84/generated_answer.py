def return_binary_or_hexa(numbers):
    if len(numbers) <= 44:
        return ''
    a = numbers[32]
    b = numbers[44]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[33:44])
    missing_numbers = full_range - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]