def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    missing_numbers = set(range(a + 1, b)) - set(numbers[20:36])
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]