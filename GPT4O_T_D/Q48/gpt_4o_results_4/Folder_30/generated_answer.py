def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    expected_range = set(range(a + 1, b))
    present_numbers = set(numbers[23:24])
    missing_numbers = expected_range - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]