def return_binary_or_hexa(numbers):
    if len(numbers) <= 200:
        return ''
    a = numbers[80]
    b = numbers[200]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[81:200])
    missing_numbers = full_range - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]