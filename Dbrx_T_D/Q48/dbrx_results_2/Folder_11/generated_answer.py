def return_binary_or_hexa(numbers):
    missing_numbers = set(range(numbers[48] + 1, numbers[76])) - set(numbers[48:76])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()