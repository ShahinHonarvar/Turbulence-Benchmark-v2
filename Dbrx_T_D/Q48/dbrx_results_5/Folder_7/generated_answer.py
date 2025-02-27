def return_binary_or_hexa(int_tuple):
    a = int_tuple[10]
    b = int_tuple[97]
    sum_of_numbers = sum(set(range(a + 1, b)) - set(int_tuple[10:98]))
    if sum_of_numbers % 2:
        return format(sum_of_numbers, 'b')
    else:
        return hex(sum_of_numbers).split('x')[-1].upper()