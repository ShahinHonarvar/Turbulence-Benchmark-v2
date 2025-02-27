def return_binary_or_hexa(input_tuple):
    a = input_tuple[2]
    b = input_tuple[5]
    if a + 1 >= b - 1:
        return ''
    non_present = set(range(a + 1, b - 1)) - set(input_tuple[3:5])
    if non_present:
        sum_val = sum(non_present)
        if sum_val % 2:
            return format(sum_val, 'b')
        else:
            return format(sum_val, 'x').upper()
    else:
        return ''