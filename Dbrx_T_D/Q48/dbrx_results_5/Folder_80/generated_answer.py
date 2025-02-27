def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[84]
    missing_numbers = set(range(a + 1, b)) - set(numbers[57:85])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()