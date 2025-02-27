def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[276:871])
    missing_numbers_sum = sum(full_range - present_numbers)
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]