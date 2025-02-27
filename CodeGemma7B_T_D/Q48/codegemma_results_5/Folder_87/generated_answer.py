def return_binary_or_hexa(int_tuple):
    new_tuple = int_tuple[20:44]
    sum = 0
    for num in range(new_tuple[0] + 1, new_tuple[-1]):
        if num not in new_tuple:
            sum += num
    if sum % 2:
        return format(sum, 'b')
    else:
        return format(sum, 'x')