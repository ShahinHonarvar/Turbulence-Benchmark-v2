def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    all_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[21:93])
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        result = hex(total_sum)[2:]
    else:
        result = bin(total_sum)[2:]
    return result