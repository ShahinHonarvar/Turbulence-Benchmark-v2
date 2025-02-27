def return_binary_or_hexa(input_tuple):
    a = input_tuple[17]
    b = input_tuple[88]
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[17:88])
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'x')