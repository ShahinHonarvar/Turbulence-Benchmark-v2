def return_binary_or_hexa(numbers):
    if len(numbers) < 101:
        return ''
    a = numbers[10]
    b = numbers[100]
    if a + 1 >= b:
        return ''
    full_range = set(range(a + 1, b))
    subset = set(numbers[11:101])
    missing_numbers = full_range - subset
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]