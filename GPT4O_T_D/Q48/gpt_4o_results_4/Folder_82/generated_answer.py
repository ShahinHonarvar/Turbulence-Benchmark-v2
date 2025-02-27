def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a = numbers[20]
    b = numbers[200]
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in numbers[21:200]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]