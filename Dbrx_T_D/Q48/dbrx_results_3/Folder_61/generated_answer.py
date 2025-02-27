def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    present_numbers = set(t[1:9])
    missing_numbers = set(range(a + 1, b)) - present_numbers
    if not missing_numbers:
        return ''
    summation = sum(missing_numbers)
    if summation % 2:
        return format(summation, '08b')
    else:
        return format(summation, 'x')