def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    full_range = set(range(a + 1, b))
    subset_range = set(numbers[45:91])
    missing_numbers = full_range - subset_range
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]