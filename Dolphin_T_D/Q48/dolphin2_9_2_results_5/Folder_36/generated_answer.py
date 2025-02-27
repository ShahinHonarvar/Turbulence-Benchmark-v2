def return_binary_or_hexa(integers_tuple):
    a = integers_tuple[110]
    b = integers_tuple[348]
    sum_of_integers = sum((x for x in range(a + 1, b) if x not in integers_tuple[110:348 + 1]))
    if sum_of_integers == 0:
        return ''
    elif sum_of_integers % 2 == 0:
        return format(sum_of_integers, 'X')
    else:
        return format(sum_of_integers, 'b')