def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    expected_numbers = set(range(a + 1, b))
    actual_numbers = set(numbers[11:28])
    missing_numbers = expected_numbers - actual_numbers
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]