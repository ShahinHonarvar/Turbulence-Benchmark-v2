def return_binary_or_hexa(input_tuple):
    a = input_tuple[70]
    b = input_tuple[200]
    sum_of_missing_numbers = sum((x for x in range(a + 1, b) if x not in input_tuple[70:201]))
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'x').upper()