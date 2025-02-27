def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[60]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[19:60])
    missing_numbers = full_range - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]