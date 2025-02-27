def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a = numbers[30]
    b = numbers[200]
    required_numbers = set(range(a + 1, b))
    available_numbers = set(numbers[31:200])
    missing_numbers = required_numbers - available_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]