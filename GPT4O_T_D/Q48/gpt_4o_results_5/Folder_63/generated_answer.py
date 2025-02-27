def return_binary_or_hexa(numbers):
    a = numbers[81]
    b = numbers[86]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[82:86])
    missing_numbers = sorted(full_range - present_numbers)
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]