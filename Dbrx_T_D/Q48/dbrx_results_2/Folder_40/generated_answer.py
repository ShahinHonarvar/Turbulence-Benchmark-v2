def return_binary_or_hexa(tup):
    all_numbers = set(range(tup[0] + 1, tup[3] - 1 + 1))
    missing_numbers = all_numbers - set(tup[1:3])
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2:
        return format(total, 'b')
    else:
        return format(total, 'x')