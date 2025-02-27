def return_binary_or_hexa(int_tuple):
    a = int_tuple[2]
    b = int_tuple[8]
    if b <= a + 1:
        return ''
    sum_not_present = sum((i for i in range(a + 1, b) if i not in int_tuple[2:9]))
    if sum_not_present % 2:
        return format(sum_not_present, 'b')
    else:
        return format(sum_not_present, 'X')