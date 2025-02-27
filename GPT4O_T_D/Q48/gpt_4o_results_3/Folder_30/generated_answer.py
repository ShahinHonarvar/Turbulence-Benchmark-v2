def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[23:24])
    missing_numbers.difference_update(present_numbers)
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2 == 0:
        return format(total, 'x')
    else:
        return format(total, 'b')