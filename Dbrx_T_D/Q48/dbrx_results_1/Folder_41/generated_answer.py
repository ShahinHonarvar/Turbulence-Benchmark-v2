def return_binary_or_hexa(numbers):
    a, b = (numbers[3], numbers[8])
    missing_numbers = set(range(a + 1, b)) - set(numbers[3:9])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()