def return_binary_or_hexa(numbers):
    if len(numbers) <= 32:
        return ''
    a = numbers[19]
    b = numbers[32]
    if b <= a + 1:
        return ''
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in numbers[20:32]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]