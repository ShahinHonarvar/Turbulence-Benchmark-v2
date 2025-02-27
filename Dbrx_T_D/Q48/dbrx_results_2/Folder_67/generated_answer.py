def return_binary_or_hexa(int_tuple):
    a = int_tuple[44]
    b = int_tuple[67]
    non_present = [x for x in range(a + 1, b) if x not in int_tuple[44:68]]
    if non_present:
        sum_val = sum(non_present)
        if sum_val % 2:
            return format(sum_val, 'b')
        else:
            return format(sum_val, 'x')
    else:
        return ''