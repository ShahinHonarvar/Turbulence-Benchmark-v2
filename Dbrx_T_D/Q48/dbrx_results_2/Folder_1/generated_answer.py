def return_binary_or_hexa(input_tuple):
    a = input_tuple[17]
    b = input_tuple[88]
    missing_numbers = [i for i in range(a + 1, b) if input_tuple.index(i) > 88]
    if not missing_numbers:
        return ''
    sum_of_numbers = sum(missing_numbers)
    if sum_of_numbers % 2:
        return format(sum_of_numbers, 'b')
    else:
        return hex(sum_of_numbers)[2:].upper()