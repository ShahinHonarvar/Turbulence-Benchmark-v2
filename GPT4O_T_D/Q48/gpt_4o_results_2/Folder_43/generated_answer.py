def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    full_range = set(range(a + 1, b))
    present_range = set(numbers[11:28])
    missing_numbers = full_range - present_range
    sum_of_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]