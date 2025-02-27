def return_binary_or_hexa(input_tuple):
    a = input_tuple[44]
    b = input_tuple[67]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in input_tuple[44:68]:
            missing_numbers.append(i)
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2 != 0:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'x').upper()