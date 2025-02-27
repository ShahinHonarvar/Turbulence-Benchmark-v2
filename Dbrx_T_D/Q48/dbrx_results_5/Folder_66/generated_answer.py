def return_binary_or_hexa(t):
    a, b = (t[11], t[76])
    present = set(t[11:77])
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - present
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    return format(sum_of_missing, 'b') if sum_of_missing % 2 else format(sum_of_missing, 'x')