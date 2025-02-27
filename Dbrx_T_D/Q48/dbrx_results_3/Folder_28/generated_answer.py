def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[86], int_tuple[99])
    non_present_sum = sum((i for i in range(a + 1, b) if i not in int_tuple[86:100]))
    if non_present_sum % 2:
        return format(non_present_sum, '08b')
    else:
        return format(non_present_sum, 'x')