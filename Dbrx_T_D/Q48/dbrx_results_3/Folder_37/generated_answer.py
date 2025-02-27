def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[7])
    sum_not_in_range = sum((i for i in range(a + 1, b) if i not in tup[2:8]))
    if sum_not_in_range % 2 != 0:
        return format(sum_not_in_range, 'b')
    else:
        return format(sum_not_in_range, 'x')