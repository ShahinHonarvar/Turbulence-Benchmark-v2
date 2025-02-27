def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[20]
    b = numbers_tuple[35]
    missing_numbers = set(range(a + 1, b)) - set(numbers_tuple[20:36])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    return '{:b}'.format(sum_of_missing) if sum_of_missing % 2 else '{:x}'.format(sum_of_missing).upper()