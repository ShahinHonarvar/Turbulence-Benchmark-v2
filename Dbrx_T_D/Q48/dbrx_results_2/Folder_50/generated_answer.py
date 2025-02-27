def return_binary_or_hexa(arg):
    a = arg[13]
    b = arg[76]
    sum_of_missing_numbers = 0
    for i in range(a + 1, b):
        if i not in arg[13:77]:
            sum_of_missing_numbers += i
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, '0b')
    else:
        return format(sum_of_missing_numbers, 'X')