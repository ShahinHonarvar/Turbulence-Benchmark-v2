def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    if b <= a + 1:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[450:906])
    missing_numbers.difference_update(present_numbers)
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, '08b')
    return hex(sum_of_missing).split('x')[-1].upper()