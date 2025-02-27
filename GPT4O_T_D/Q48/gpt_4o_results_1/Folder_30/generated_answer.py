def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    required_numbers = set(range(a + 1, b))
    given_numbers = set(numbers[23:24])
    missing_numbers = required_numbers - given_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]