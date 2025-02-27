def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    range_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[91:200])
    missing_numbers = range_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]