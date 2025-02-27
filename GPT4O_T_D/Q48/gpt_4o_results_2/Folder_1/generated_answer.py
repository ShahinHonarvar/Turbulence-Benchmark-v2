def return_binary_or_hexa(numbers):
    if len(numbers) <= 88:
        return ''
    a = numbers[17]
    b = numbers[88]
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in numbers[17:89]))
    if missing_numbers_sum == 0:
        return ''
    return bin(missing_numbers_sum)[2:] if missing_numbers_sum % 2 else hex(missing_numbers_sum)[2:]