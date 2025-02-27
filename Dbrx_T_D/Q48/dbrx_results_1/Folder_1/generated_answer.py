def return_binary_or_hexa(input_tuple):
    a = input_tuple[17]
    b = input_tuple[88]
    if a + 1 > b - 1:
        return ''
    sum_of_elements = sum(range(a + 1, b))
    if sum_of_elements % 2 != 0:
        return format(sum_of_elements, '08b')
    else:
        return format(sum_of_elements, '02x').upper()