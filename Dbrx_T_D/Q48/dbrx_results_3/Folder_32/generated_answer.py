def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    missing_numbers = list(set(range(a + 1, b)) - set(numbers[86:91]))
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()