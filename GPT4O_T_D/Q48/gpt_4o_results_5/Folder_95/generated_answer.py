def return_binary_or_hexa(t):
    if len(t) < 100:
        return ''
    a = t[32]
    b = t[99]
    full_range = set(range(a + 1, b))
    missing_numbers = full_range.difference(t[33:100])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')