def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    full_range = set(range(a + 1, b))
    subset = set(numbers[21:51])
    missing_numbers = full_range - subset
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]