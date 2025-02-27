def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    required_numbers = set(range(a + 1, b))
    existing_numbers = set(numbers[50:74])
    missing_numbers = required_numbers - existing_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]