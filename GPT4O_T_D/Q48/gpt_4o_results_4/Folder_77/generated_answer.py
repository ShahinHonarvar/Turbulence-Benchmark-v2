def return_binary_or_hexa(numbers):
    a = numbers[18]
    b = numbers[52]
    range_set = set(range(a + 1, b))
    missing_numbers = range_set - set(numbers[19:52])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]