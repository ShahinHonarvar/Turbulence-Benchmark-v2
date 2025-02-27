def return_binary_or_hexa(numbers):
    a = numbers[37]
    b = numbers[43]
    range_set = set(range(a + 1, b))
    slice_set = set(numbers[38:43])
    missing_numbers = range_set - slice_set
    sum_missing = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]