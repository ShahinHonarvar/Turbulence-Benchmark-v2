def return_binary_or_hexa(integer_tuple):
    if len(integer_tuple) < 100 or integer_tuple[67] >= integer_tuple[98]:
        return ''
    a, b = (integer_tuple[67], integer_tuple[98])
    missing_numbers = set(range(a + 1, b))
    missing_numbers.difference_update(integer_tuple[68:99])
    if not missing_numbers:
        return ''
    summation = sum(missing_numbers)
    if summation % 2:
        return format(summation, 'b')
    else:
        return hex(summation)[2:].upper()