def return_binary_or_hexa(numbers):
    if len(numbers) <= 51:
        return ''
    a = numbers[20]
    b = numbers[51]
    needed_numbers = set(range(a + 1, b))
    existing_numbers = set(numbers[21:51])
    missing_numbers = needed_numbers - existing_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]