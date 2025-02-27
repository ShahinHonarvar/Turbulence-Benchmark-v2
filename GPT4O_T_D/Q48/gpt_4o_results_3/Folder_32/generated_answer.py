def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    expected_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[87:90])
    missing_numbers = expected_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]