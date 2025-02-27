def return_binary_or_hexa(numbers):
    if len(numbers) <= 97:
        return ''
    a = numbers[10]
    b = numbers[97]
    range_set = set(range(a + 1, b))
    numbers_set = set(numbers[11:97])
    missing_numbers = range_set - numbers_set
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]