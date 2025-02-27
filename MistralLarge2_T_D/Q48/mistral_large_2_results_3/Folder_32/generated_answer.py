def return_binary_or_hexa(numbers):
    if len(numbers) < 91:
        return ''
    a = numbers[86]
    b = numbers[90]
    missing_numbers = set(range(a + 1, b)) - set(numbers[86:91])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]