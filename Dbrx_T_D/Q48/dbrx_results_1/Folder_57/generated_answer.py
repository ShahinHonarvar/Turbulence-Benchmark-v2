def return_binary_or_hexa(input_tuple):
    a = input_tuple[24]
    b = input_tuple[79]
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[25:80])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')