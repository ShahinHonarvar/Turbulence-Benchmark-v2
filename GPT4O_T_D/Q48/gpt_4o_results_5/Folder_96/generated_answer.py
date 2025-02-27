def return_binary_or_hexa(numbers):
    if len(numbers) <= 200:
        return ''
    a = numbers[50]
    b = numbers[200]
    all_numbers = set(range(a + 1, b))
    existing_numbers = set(numbers[51:200])
    missing_numbers = all_numbers - existing_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]