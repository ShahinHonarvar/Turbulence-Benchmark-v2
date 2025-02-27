def return_binary_or_hexa(numbers):
    if len(numbers) < 201:
        return ''
    a = numbers[70]
    b = numbers[200]
    full_range = set(range(a + 1, b))
    subset_range = set(numbers[71:200])
    missing_numbers = full_range - subset_range
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]