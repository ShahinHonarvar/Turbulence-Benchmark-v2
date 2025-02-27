def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[51], num_tuple[76])
    summation = 0
    for num in range(a + 1, b):
        if num not in num_tuple[51:77]:
            summation += num
    if summation % 2:
        return format(summation, 'b')
    else:
        return format(summation, 'x')