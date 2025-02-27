def return_binary_or_hexa(input_tuple):
    a = input_tuple[19]
    b = input_tuple[32]
    present_numbers = set(input_tuple[19:33])
    missing_numbers = set(range(a + 1, b))
    if missing_numbers.issubset(present_numbers):
        return ''
    sum_of_missing_numbers = sum(missing_numbers - present_numbers)
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'X')