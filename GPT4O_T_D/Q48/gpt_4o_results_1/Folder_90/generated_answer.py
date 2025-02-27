def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[90]
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in numbers[61:90]))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    return hex(missing_numbers_sum)[2:]