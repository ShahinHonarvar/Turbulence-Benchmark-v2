def return_binary_or_hexa(num_tuple):
    a = num_tuple[1]
    b = num_tuple[4]
    sum_of_integers = sum((i for i in range(a + 1, b) if i not in num_tuple[1:4]))
    sum_is_odd = sum_of_integers % 2 != 0
    if all((i in num_tuple[1:4] for i in range(a + 1, b))):
        return ''
    return format(sum_of_integers, 'b' if sum_is_odd else 'x')