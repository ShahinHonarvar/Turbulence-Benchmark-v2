def return_binary_or_hexa(int_tuple):
    a = int_tuple[7]
    b = int_tuple[9]
    sum_of_missing = sum(set(range(a + 1, b)) - set(int_tuple[7:10]))
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')