def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    start = a + 1
    end = b
    sum_missing = 0
    numbers_in_range = set(numbers[428:670])
    missing_numbers = set(range(start, end)) - numbers_in_range
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]