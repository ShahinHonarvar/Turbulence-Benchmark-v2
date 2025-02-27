def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    full_range = set(range(a + 1, b))
    present_range = set(numbers[21:43])
    missing_numbers = full_range - present_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]