def return_binary_or_hexa(input_tuple):
    a = input_tuple[36]
    b = input_tuple[85]
    sum_of_numbers = sum((i for i in range(a + 1, b) if i not in input_tuple))
    if sum_of_numbers % 2 != 0:
        return format(sum_of_numbers, 'b')
    else:
        return format(sum_of_numbers, 'x')