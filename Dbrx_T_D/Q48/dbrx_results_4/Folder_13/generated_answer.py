def return_binary_or_hexa(numbers):
    a, b = (numbers[45], numbers[90])
    missing_numbers = set(range(a + 1, b)) - set(numbers[46:91])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()