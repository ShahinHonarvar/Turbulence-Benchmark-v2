def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    all_numbers = set(range(a + 1, b))
    numbers_in_range = set(numbers[14:76])
    missing_numbers = all_numbers - numbers_in_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]