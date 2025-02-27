def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[7], int_tuple[9])
    missing_numbers = set(range(a + 1, b)) - set(int_tuple[8:9])
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    return format(total, 'b') if total % 2 else format(total, 'x')