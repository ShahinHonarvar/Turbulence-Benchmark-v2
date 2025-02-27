def return_binary_or_hexa(int_tuple):
    a = int_tuple[110]
    b = int_tuple[348]
    if a >= b:
        return ''
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(int_tuple[110:349])
    missing_numbers -= present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'X')