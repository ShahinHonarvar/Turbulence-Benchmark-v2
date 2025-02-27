def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    required_range = set(range(a + 1, b))
    present_numbers = set(numbers[38:43])
    missing_numbers = required_range - present_numbers
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]