def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    required_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[201:202])
    missing_numbers = required_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]