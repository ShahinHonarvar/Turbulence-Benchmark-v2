def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    full_range = set(range(a + 1, b))
    missing_numbers = full_range - set(numbers[0:9])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        result = hex(total_sum)[2:]
    else:
        result = bin(total_sum)[2:]
    return result