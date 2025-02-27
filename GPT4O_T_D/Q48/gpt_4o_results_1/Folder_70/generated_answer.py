def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    full_range = set(range(a + 1, b))
    missing_numbers = full_range - set(numbers[44:70])
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]