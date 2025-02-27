def return_binary_or_hexa(numbers):
    a = numbers[29]
    b = numbers[53]
    numbers_set = set(numbers[30:53])
    missing_numbers_sum = sum((i for i in range(a + 1, b) if i not in numbers_set))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 0:
        return hex(missing_numbers_sum)[2:]
    else:
        return bin(missing_numbers_sum)[2:]