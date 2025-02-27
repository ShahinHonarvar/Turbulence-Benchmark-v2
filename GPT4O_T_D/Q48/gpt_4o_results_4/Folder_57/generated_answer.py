def return_binary_or_hexa(t):
    a = t[25]
    b = t[80]
    candidates = set(range(a + 1, b))
    tuple_subset = set(t[26:80])
    missing_numbers = candidates - tuple_subset
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')