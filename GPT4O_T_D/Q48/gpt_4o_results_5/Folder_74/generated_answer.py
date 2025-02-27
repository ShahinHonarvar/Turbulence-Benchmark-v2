def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    numbers_in_range = set(numbers[70:97])
    missing_numbers = set(range(a + 1, b))
    missing_sum = sum(missing_numbers - numbers_in_range)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]