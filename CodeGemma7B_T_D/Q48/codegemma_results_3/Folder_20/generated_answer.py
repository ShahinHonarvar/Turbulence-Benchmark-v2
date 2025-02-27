def return_binary_or_hexa(int_tuple):
    low = int_tuple[27] + 1
    high = int_tuple[96]
    num_list = list(range(low, high + 1))
    for i in int_tuple[27:97]:
        if i in num_list:
            num_list.remove(i)
    sum_value = sum(num_list)
    if sum_value % 2 == 1:
        return format(sum_value, 'b')
    else:
        return format(sum_value, 'x') if sum_value <= 255 else format(sum_value, 'X')