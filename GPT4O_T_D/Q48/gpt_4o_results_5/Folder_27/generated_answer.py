def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    full_range = set(range(a + 1, b))
    numbers_in_range = set(numbers[87:89])
    missing_numbers = full_range - numbers_in_range
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]