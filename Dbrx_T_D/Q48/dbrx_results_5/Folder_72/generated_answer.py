def return_binary_or_hexa(int_tuple):
    a = int_tuple[13]
    b = int_tuple[70]
    missing_set = set(range(a + 1, b))
    present_set = set(int_tuple[13:71])
    missing_set.difference_update(present_set)
    if not missing_set:
        return ''
    sum_of_missing = sum(missing_set)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x')