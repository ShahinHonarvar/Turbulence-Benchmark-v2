def return_binary_or_hexa(numbers):
    if len(numbers) <= 64:
        return ''
    a = numbers[35]
    b = numbers[64]
    if b - a <= 1:
        return ''
    full_range = set(range(a + 1, b))
    present_numbers = set(numbers[36:64])
    missing_numbers = full_range - present_numbers
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]