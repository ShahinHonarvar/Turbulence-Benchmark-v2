def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    full_range = set(range(a + 1, b))
    tuple_subset = set(numbers[45:91])
    missing_numbers = full_range - tuple_subset
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]