def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[6]
    full_range = set(range(a + 1, b))
    missing_numbers = full_range - set(numbers[1:7])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]